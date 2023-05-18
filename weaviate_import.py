import weaviate
import json

classes= ['Track']#, 'Artist', 'Album']

def init_client():
    client = weaviate.Client(
        url="http://localhost:8080",  # Replace with your endpoint
    )

    # Import class schemas
    class_paths = ["schema/track_class.json"] #, "schema/artist_class.json", "schema/album_class.json"]

    for path in class_paths:
        with open(path, "r") as f:
            class_obj = json.load(f)
        # Create classes
        try:
            client.schema.create_class(class_obj)
        except:
            print(f"class {path} already exists")
    
    return client

def delete_class(client, class_name="Songs"):
    try:
        client.schema.delete_class(class_name)
    except:
        print(f"class {class_name} does not exist")

def read_data():
    # Read the data
    with open("data/spotify_songs.json", "r") as f:
        data = json.load(f)
    return data

def import_data(client, data):

    # flush the schema and data
    client.schema.delete_all()
    # cut data
    # data = data[:10]

    # Configure a batch 
    with client.batch as batch:
        batch.batch_size=100
        # Batch import all tracks
        for i, d in enumerate(data):
            print(f"importing track: {i+1}")

            track_properties = {
                "track_name": d["track_name"],
                "track_id": d["track_id"],
                "lyrics": d["lyrics"],
                "track_popularity": d["track_popularity"],
                "genre": d["playlist_genre"],
                "subgenre": d["playlist_subgenre"],
                "danceability": d["danceability"],
                "energy": d["energy"],
                "key": d["key"],
                "loudness": d["loudness"],
                "mode": d["mode"],
                "speechiness": d["speechiness"],
                "acousticness": d["acousticness"],
                "instrumentalness": d["instrumentalness"],
                "liveness": d["liveness"],
                "valence": d["valence"],
                "tempo": d["tempo"],
                "duration_ms": d["duration_ms"],
                "album_name": d["track_album_name"],
                "album_id": d["track_album_id"],
                "album_release_date": d["track_album_release_date"],
                "artist_name": d["track_artist"]
                }

            # artist_properties = {
            #     "name": d["track_artist"]
            # }

            # album_properties = {
            #     "name": d["track_album_name"],
            #     "album_id": d["track_album_id"],
            #     "releas_date": d["track_album_release_date"],
            # }

            client.batch.add_data_object(track_properties, "Track")
            # client.batch.add_data_object(artist_properties, "Artist")
            # client.batch.add_data_object(album_properties, "Album")

def query(client):
    where_filter = {
        "path": ["popularity"],
        "operator": "GreaterThan",
        "valueNumber": "80"
    }
    nearText = {
        "concepts": ["Galileo"],
    }  

    result = ( 
        client.query
        .get("Track", ["track_name"])
        # .with_where(where_filter)
        .with_near_text(nearText)
        .with_limit(2)
        .do()
    )

    print(json.dumps(result, indent=4))

def ask(client):
    ask = {
        "question": "Ariana Grande?",
        "properties": ["name"],
    }

    result = (
        client.query
        .get("Track", ["name", "_additional {answer {hasAnswer certainty property result startPosition endPosition} }"])
        .with_ask(ask)
        .with_limit(1)
        .do()
        )
    print(json.dumps(result, indent=4))

def main(args):
    client = init_client()
    # data = read_data()
    # import_data(client, data)
    query(client)
    # ask(client)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Import data for weaviate.")
    args = parser.parse_args()

    main(args)
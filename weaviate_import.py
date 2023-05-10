import weaviate
import json

def init_client():
    client = weaviate.Client(
        url="http://localhost:8080",  # Replace with your endpoint
    )

    # Import class schemas
    with open("schema/track_class.json", "r") as f:
        track_class_obj = json.load(f)
    # Create classes
    classes = [track_class_obj]

    # Create classes
    try:
        for c in classes:
            client.schema.create_class(c)
    except:
        print("class already exists")
    
    return client

def delete_class(client, class_name="Songs"):
    client.schema.delete_class(class_name)

def read_data():
    # Read the data
    with open("data/spotify_songs.json", "r") as f:
        data = json.load(f)
    return data

def import_data(client, data):
    # Configure a batch process
    with client.batch as batch:
        batch.batch_size=100
        # Batch import all tracks
        for i, d in enumerate(data):
            print(f"importing track: {i+1}")

            properties = {
                "track_name": d["track_name"],
                "track_artist": d["track_artist"],
                "track_id": d["track_id"],
                "lyrics": d["lyrics"],
                "track_popularity": d["track_popularity"],
                "album_id": d["track_album_id"],
                "album_name": d["track_album_name"],
                "album_release_date": d["track_album_release_date"],
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
            }
            client.batch.add_data_object(properties, "Track")

def query(client):
    where_filter = {
        "path": ["track_popularity"],
        "operator": "GreaterThan",
        "valueNumber": "80"
    }
    nearText = {
        "concepts": ["Galileo"],
    }  

    result = ( 
        client.query
        .get("Track", ["track_name", "track_artist", "track_popularity"])
        .with_where(where_filter)
        .with_near_text(nearText)
        .with_limit(2)
        .do()
    )

    print(json.dumps(result, indent=4))

def main(args):
    client = init_client()
    # delete_class(client, 'Track')
    # data = read_data()  
    # import_data(client, data)
    # query(client)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Import data for weaviate.")
    args = parser.parse_args()

    main(args)
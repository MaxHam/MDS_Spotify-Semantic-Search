import weaviate
import json

def init_client():
    client = weaviate.Client(
        url="http://localhost:8080",  # Replace with your endpoint
    )

    class_obj = {
        "class": "Songs",
        "vectorizer": "text2vec-contextionary" #  runs in docker-compose
    }

    try:
        client.schema.create_class(class_obj)
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
        # Batch import all Questions
        for i, d in enumerate(data):
            print(f"importing song: {i+1}")

            properties = {
                "track_name": d["track_name"],
                "track_artist": d["track_artist"],
                "track_id": d["track_id"],
                "lyrics": d["lyrics"],
                "track_popularity": d["track_popularity"],
                "track_album_id": d["track_album_id"],
                "track_album_name": d["track_album_name"],
                "track_album_release_date": d["track_album_release_date"],
                "playlist_name": d["playlist_name"],
                "playlist_id": d["playlist_id"],
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
            client.batch.add_data_object(properties, "Songs")

def query(client):
    # where_filter = {
    #     "path": ["track_id"],
    #     "operator": "Equal",
    #     "valueString": "1AhDOtG9vPSOmsWgNW0BEY"
    # }
    nearText = {
        "concepts": ["mama"],
    }  

    result = ( 
        client.query
        .get("Songs", ["lyrics"])
        .with_near_text(nearText)
        # .with_where(where_filter)
        .with_limit(10)
        .do()
    )

    print(json.dumps(result, indent=4))

def main(args):
    client = init_client()
    delete_class(client, 'Songs')
    data = read_data()  
    import_data(client, data)
    query(client)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Import data for weaviate.")
    args = parser.parse_args()

    main(args)
import weaviate
import json
from datetime import datetime, timezone

classes= ['Track']

def init_client():
    client = weaviate.Client(
        url="http://localhost:8081",  # Replace with your endpoint
    )
    
    return client

def delete_class(client, class_name="Track"):
    try:
        client.schema.delete_class(class_name)
        print(f"class {class_name} deleted")
    except:
        print(f"class {class_name} does not exist")

def read_data():
    # Read the data
    with open("data/spotify_songs.json", "r") as f:
        data = json.load(f)
    return data

def create_schema(client, data):
    # flush the schema and data
    delete_class(client, "Track")

    # Import class schemas
    class_paths = ["schema/track_class.json"]
    for path in class_paths:
        with open(path, "r") as f:
            class_obj = json.load(f)
        # Create classes
        try:
            print(f"Create new class schema! {path}")
            client.schema.create_class(class_obj)
        except Exception as e:
            print(e)

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def import_data(client, data):

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
                # "album_release_date": parse_date(d["track_album_release_date"]).isoformat(),
                "artist_name": d["track_artist"]
                }
            
            client.batch.add_data_object(track_properties, "Track")

def main():
    client = init_client()
    data = read_data()
    create_schema(client, data)
    schema = client.schema.get()
    print(schema)
    import_data(client, data)



if __name__ == "__main__":
    main()
# import weaviate
# import json

# client = weaviate.Client(
#     url="http://localhost:8080",  # Replace with your endpoint
# )

# class_obj = {
#     "class": "Songs",
#     "vectorizer": "text2vec-transformers" #  runs in docker-compose
# }
# # client.schema.delete_class("Songs")
# client.schema.create_class(class_obj)

# # # Read the data
# with open("data/spotify_songs.json", "r") as f:
#     data = json.load(f)

# # Configure a batch process
# with client.batch as batch:
#     batch.batch_size=10
#     # Batch import all Questions
#     for i, d in enumerate(data):
#         print(f"importing song: {i+1}")

#         properties = {
#             "track_name": d["track_name"],
#             "track_artist": d["track_artist"],
#             "track_id": d["track_id"],
#             "lyrics": d["lyrics"],
#         }
#         client.batch.add_data_object(properties, "Songs")
# Load data
import weaviate
import json

client = weaviate.Client(
    url = "http://localhost:8080",  # Replace with your endpoint
    # auth_client_secret=weaviate.auth.AuthApiKey(api_key="YOUR-WEAVIATE-API-KEY"),  # Replace w/ your Weaviate instance API key
    # additional_headers = {
    #     "X-OpenAI-Api-Key": "YOUR-OPENAI-API-KEY"  # Replace with your inference API key
    # }
)

# ===== add schema =====
class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-transformers"
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)

# ===== import data =====
# Load data
import requests
url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
with client.batch as batch:
    batch.batch_size=100
    # Batch import all Questions
    for i, d in enumerate(data):
        print(f"importing question: {i+1}")

        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        client.batch.add_data_object(properties, "Question")
# Music Similarity Search

## Table of contents
- [Motivation](#motivation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Benchmark](#benchmark)
- [Dataset](#dataset)
- [Authors](#authors)

# Motivation
This is a project for the "Modern Database Systems" lecture, held at the Technische Hochschule Köln. Aim of the project is to find a use case where modern NoSQL databases outperform SQL databases.
We decided to build a music similarity search engine, where you can search for a song and get similar songs back. The similarity is based on the lyrics and the audio features of the song. The project is based on the [Spotify Dataset](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs) from Kaggle.
# Requirements
- Node.js
- Docker
- Python 3.8
- Spotify API credentials
## Installation
1. Install the requirements with
```bash
pip install -r requirements.txt
```
2. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)
3. Unzip the dataset and place it in the `data` directory

4. Clean the dataset with 
```bash
python3 clean_data.py
```

5. Create an `.env` file in the `webapp` directory with the following content. You need this to enable the Spotify API. You need to set up a spotify application. Look [here](https://developer.spotify.com/documentation/web-api/concepts/apps) for more information.
```bash
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
PORT=5001
```

6. First time using this project create the Weaviate.io & vectorizer server containers and start the web server with
```bash
docker-compose up
```

7. Import the dataset into Weaviate.io with
```bash
python weaviate_import.py
```

8. Go to `localhost:3000` and enjoy listening to songs!
## Benchmark

1. If not already done, repeat all steps mentioned in [Installation](#installation) to initiliaze the vector database

2. Clean the dataset with clean_sql_data and create the required .sql script
```bash
python3 clean_sql_data.py
```

3. Upload the dataset to the sql server
```bash
python3 sql_import.py
```

4. Run the benchmark script and see the results in the console or in the `benchmark_results.csv` file
```bash
python3 benchmark.py
```

## Dataset
[Spotify Dataset](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)

## Authors
- Max Hammer
- Dennis Goessler
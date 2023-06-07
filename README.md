# Music Similarity Search
This is a project for the "Modern Database Systems" lecture, held at the Technische Hochschule Köln. Aim of the project is to find a use case where modern NoSQL databases outperform SQL databases.

## Table of contents
- [Motivation](#motivation)
- [Roadmap](#roadmap)
- [Requirements](#requirements)
- [Installation](#installation)
- [Benchmark](#benchmark)
- [Dataset](#dataset)
- [Databases](#databases)
- [Helpful](#helpful)
- [Other interesting datasets](#other-interesting-datasets)
## Motivation

> Music Dataset consists of 25 columns, describing track_id, track_name, artist_name, album_names, genre, release_date, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature, lyrics, language, lyrics_sentiment, lyrics_subjectivity, lyrics_polarity.
Feed these into a vector format to find a similar song by selecting a song from the existing dataset.

### Use cases:

- Recommend user a song based on other interests.
- Use database to write song lyrics in style of songs
- Categorize Songs extending classic keywords like artist, song title, genre
- Find similar songs based on lyrics
- Find similar songs based on audio features
- Find similar songs based on both lyrics and audio features
- Find songs with natural language search

## Roadmap
- [x] Create a vector database with Weaviate.io
- [x] Create SQL schema
- [x] Create a SQL database
- [ ] Create index in the SQL database
- [x] Optimize Weaviate.io schema
- [x] Create a frontend
- [x] Integrate Weaviate.io with frontend
- [ ] Integrate SQL database with frontend
- [x] Semantic search with Weaviate.io
- [ ] Keyword search with SQL
- [x] Similarity Search
- [ ] ~~Create a generative~~ search engine
- [x] Integrate Spotify API
- [x] Dockerize frontend
- [x] Update docker-compose

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

5. Create an `.env` file in the `webapp` directory with the following content. You need this to enable the Spotify API.
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

4. Run the benchmark script
```bash
python3 benchmark.py
```

## Dataset

[Spotify Dataset](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)

## Databases
Decide for a database that fits use case the best.
### [Weaviate.io](https://weaviate.io/?utm_source=google&utm_medium=cpc&utm_campaign=18703782893&utm_content=142806251237&utm_term=weaviate%20database&gclid=CjwKCAjwl6OiBhA2EiwAuUwWZeSv5162-ikjmZwHUoACgHfJjNiNXGfvP3a1GaWv4CTS3Sr6gq2syxoCbwsQAvD_BwE)

- vector database
- open-source
- integrated embedding model
- vector search
- **generative search**
- GraphQL scheme
- vector-native
- semantic search

### [Elasticsearch](https://www.elastic.co/de/elasticsearch/)

- established database
- vector search
- no scheme
- document-oriented
- real-time
- allow multiple indexes for search (e.g. similarity across all attributes, similarity in text,title)

**WINNER** Weaviate.io, because
- we want to build a vector search engine and it is vector-native.
- we want to integrate natural language search and the database offers direct integration of a generative search engine.
## Helpful

- [https://www.kaggle.com/code/nikil42516/plot-based-music-recommender-system](https://www.kaggle.com/code/nikil42516/plot-based-music-recommender-system)
- [https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html](https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html)
- https://github.com/sheacon/semantic_song_search/blob/main/research_paper_v1.pdf

### Other interesting datasets

[Political news articles | Webz.io](https://webz.io/free-datasets/political-news-articles/)

[Reddit Memes Dataset](https://www.kaggle.com/datasets/sayangoswami/reddit-memes-dataset)

[Music Dataset : 1950 to 2019](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019)

[Audio features and lyrics of Spotify songs](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)
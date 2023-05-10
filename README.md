# Music Similarity Search
## Motivation

> Music Dataset consists of 25 columns, describing track_id, track_name, artist_name, album_names, genre, release_date, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature, lyrics, language, lyrics_sentiment, lyrics_subjectivity, lyrics_polarity.
Feed these into a vector format to find a similar song by selecting a song from the existing dataset.

Use cases:

- Recommend user a song based on other interests.
- Use database to write song lyrics in style of songs
- Categorize Songs extending classic keywords like artist, song title, genre
- Find similar songs based on lyrics
- Find similar songs based on audio features
- Find similar songs based on both lyrics and audio features
- Find songs with natural language search
## Dataset

[Spotify Dataset](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)
[Music Dataset : 1950 to 2019](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019)

[Audio features and lyrics of Spotify songs](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)

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

### Other interesting datasets

[Political news articles | Webz.io](https://webz.io/free-datasets/political-news-articles/)

[Reddit Memes Dataset](https://www.kaggle.com/datasets/sayangoswami/reddit-memes-dataset)
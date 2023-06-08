# Paper

## Graphs
- Project Architecture (draw.io)
- Cosine Similarity
- t-SNE





# Arguments for Weaviate.io
## Pros
- do not have to worry about data types
- exploratory search
- > Q: What is the difference between Weaviate and for example Elasticsearch?
A: Other database systems like Elasticsearch rely on inverted indices, which makes search super fast. Weaviate also uses inverted indices to store data and values. But additionally, Weaviate is also a vector-native search database, which means that data is stored as vectors, which enables semantic search. This combination of data storage is unique, and enables fast, filtered and semantic search from end-to-end.
https://weaviate.io/developers/weaviate/more-resources/faq
## Cons
- hard to integrate complex class structure, because of cross references
- no keyword search
# Arguments for SQL

## Pros

## Cons
- when quering with `%test%` we lose index and have to scan the whole table

# Paper
## Outline
1. Introduction
    - Motivation
    - Use case
    - Features
    - Dataset
    - Outline
2. Project
    - Use case
    - Architecture
    - Implementation
3. Data
    - Dataset
    - data cleaning
    - data schema
4. Weaviate as Vector Database
    - General
    - Semantic Search
        - how it works
    - Similarity recommendation
        - how it works
    
3. Discussion Database comparison
    - compare SQL vs. Weaviate
    - compare use case
    - compare speed
    - compare maintainability
        - migration
    - compare scalability
        - horizontal vs vertical
    - compare complexity
    - compare cost
    - compare flexibility
5. Conclusion
    - Summary
    - Future work
    - Limitations
    - Outlook



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
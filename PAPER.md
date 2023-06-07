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
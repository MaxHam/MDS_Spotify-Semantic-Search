import json
from weaviate_import import init_client
from timeit import default_timer as timer


def vector_query(client, query, limit=10):

    nearText = {
        "concepts": query,
    }  

    result = ( 
        client.query
        .get("Track", ["track_name"])
        # .with_where(where_filter)
        .with_near_text(nearText)
        .with_limit(limit)
        .do()
    )

    return result

def aggregate_query_time(func, n=100):
    '''
    Aggregate the query time for a function
    '''
    total_time = 0
    for i in range(n):
        time = measure(func)
        total_time += time
        print (f"Query {i}/{n} took {time} seconds")
    return total_time / n

def measure(func):
    '''
    Measure execution time of a function
    '''
    start = timer()

    func()

    end = timer()
    return end - start

def main(args):
    '''
    Benchmark weaviate vs. SQL similiarity query performance
    Query the databases and measure the execution time
    for Vector, Document and SQL databases.
    Columns to query: track_name, artist_name, album_name, lyrics, genre, subgenre
    - Single word query e.g. "Love"
    - Multiple text query e.g. ["Love", "Cake", "Galileo"]
    - Full sentence query e.g. "What is love?"
    - Singular Column query e.g. "track_name" == "What is love?" (Indexed)
    - Full Track similarity query e.g. {"track_name": "What is love?", "artist_name": "Haddaway"} 

    
    Run benchmark 100x and take the average 
    We evaluate the quality of results ourselves
    '''

    # init dbs
    weaviate_client = init_client()
    sql_client = None

    # Query for 50 tracks that are "similar" to "What is love?"
    query = ["What is love?"]
    # Measure single query time for vector database
    print("Measuring single query times...")
    query_time = aggregate_query_time(lambda: vector_query(weaviate_client, query=query, limit=50))
    print(f"Single Query time for vector database: {query_time}")
    # Measure query time for SQL database
    # query_time = measure(lambda: query(sql_client))
    # print(f"Single Query time for SQL database: {query_time}")

    # print("Measuring multiple query times...")
    # # Query for 50 tracks that are "similar" to multiple queries
    # mul_query = ["What is love?", "Galileo", "Birthday cake"]
    # # Measure multiple query time for vector database
    # query_time = measure(lambda: query(weaviate_client, query=mul_query, limit=50))
    # print(f"Multiple Query time for vector database: {query_time}")
    # # Measure multiple query time for SQL database
    # query_time = measure(lambda: query(sql_client))
    # print(f"Multiple Query time for SQL database: {query_time}")

    # # Query for 50 tracks that are "similar" to a whole track
    # track_query = ["What is love?"]
    # # Measure  query time for vector database
    # query_time = measure(lambda: query(weaviate_client, query=track_query, limit=50))
    # print(f"Track Query time for vector database: {query_time}")
    # # Measure query time for SQL database
    # query_time = measure(lambda: query(sql_client))
    # print(f"Track Query time for SQL database: {query_time}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Benchmark weaviate vs. SQL query performance")
    args = parser.parse_args()

    main(args)
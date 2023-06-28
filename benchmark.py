import json
import pandas as pd
import mysql.connector
from datetime import datetime
from weaviate_import import init_client
from timeit import default_timer as timer
from utils import add_limit, build_sql_query, get_operands, get_track_names, save_results

# Example: Queen - Get Down, Make Love - Remastered 2011
example_vector = [-0.06430846, -0.24293041, 0.110439375, -0.100999914, 0.09629649, -0.04072969, -0.169328, -0.014131491, 0.117915705, 0.5358003, 0.13591173, 0.1179824, -0.08689239, 0.060807075, 0.09822265, 0.19681141, -0.14886066, 0.060191516, -0.46446335, -0.016015284, 0.06305353, 0.14932896, -0.25746924, 0.1558214, -0.2350968, -0.44718155, 0.27163702, -0.54405105, -0.09141091, 0.050858628, 0.34632823, 0.48786363, 0.32426932, 0.5739468, 0.23869427, -0.3895692, 0.04086138, 0.30526224, -0.09721386, 0.7694963, -0.23109816, 0.25778306, 0.06246513, -0.15824226, -0.07554409, 0.4262448, 0.3915728, -0.10568536, -0.3647673, 0.012407957, -0.6349575, -0.2149216, -0.2833733, -0.45024365, -0.09075926, 0.13799985, -0.096156955, -0.15037905, 0.1893991, 0.1821173, 0.57067454, -0.8982235, -0.4192168, -0.25409874, 0.298224, -0.22855514, -0.17255244, -0.2956281, -0.19140317, -0.08400424, -0.14878975, 0.08089396, 0.11062146, -0.19968952, 0.5094097, -0.5838567, -0.17085947, 0.096286826, 0.2912769, 0.11041665, -0.09463574, -0.781021, 0.15997428, 0.11306844, 0.78838485, 0.046952806, 0.20534825, -0.013530162, 0.13570505, 0.39102194, -0.01179285, 0.21663925, -0.24078456, 0.30120635, -0.027091846, 0.14774093, -0.29773268, -0.42512724, -0.11435961, 0.18203783, -0.41414407, -0.20505615, 0.8132204, 0.018949207, -0.14595698, -0.15278365, -0.112690575, -0.5838136, -0.21263546, -0.13692501, -0.008073677, -0.13169445, 0.24559294, 0.11468319, -0.30848005, -0.56463796, 0.080196455, -0.13245742, -0.1404417, 0.081029356, 0.18065631, 0.31255183, 0.10336783, 0.13753967, 0.022072855, 0.14859243, 1.6029545, 0.46531165, -0.20865615, 0.012292662, 0.15616858, -0.45227888, -0.77387786, -0.43062842, 0.016371612, 0.3711838, 0.5039181, 0.15240684, -0.1913129, -0.27780148, -0.009997403, 0.117378555, -0.0085565215, -0.07294885, -0.024712797, 0.42950535, -0.005417766, -0.041284315, -0.1248916, -0.09128173, 0.345162, 0.2769205, -0.3914345, 0.057552766, -0.027560443, 0.5258812, 0.10822242, 0.31862304, -0.6082464, -0.22113307, -0.6233102, -0.34389177, -0.1452825, -0.1252571, -0.12338128, 0.4402884, 0.34804556, -0.13827753, -0.08136732, -0.306151, -0.18906707, 0.39232698, -0.09769015, 0.18603276, -0.517225, -0.7027275, 0.034595076, -0.24334815, 0.17681517, 0.28136656, -0.35619092, -1.133969, 0.057308406, -0.5783666, 0.10168155, -0.109514184, -0.23636238, 0.091893405, 0.086915925, 0.54031307, 0.13154425, 0.39741704, 0.17699283, 0.339236, -0.2782195, 0.0015203763, -0.29165968, 0.35996062, -0.083890885, -0.030090114, -0.43646154, -0.17463323, 0.40066385, -0.087886214, -0.18553457, 0.39516634, 0.26139808, -0.31970882, 0.35820448, 0.10034503, -0.3061243, -0.036659196, -0.10865491, 0.4053416, -0.11471894, 0.43889588, 0.36892733, -0.12887777, 0.055665467, -0.047561377, -0.109102905, -0.08950873, -0.057528242, -0.2530506, 0.1425888, -0.11001377, -0.5834436, 0.20523982, -0.23291121, -0.41186935, -0.23352517, -0.41898695, 0.24615884, 0.63720244, 0.08238311, -0.32418433, 0.19017169, 0.3589935, 0.12049238, 0.33731705, -0.01893071, -0.1797846, 0.4786759, 0.20034383, 0.18493232, 0.09827406, 0.14285572, -0.17101601, 0.46751156, 0.12339927, -0.076471925, 0.2264648, 0.43471265, 0.10593008, 0.2955751, -0.08592804, -0.2486908, 0.091301665, -0.5648791, 0.036137637, 0.025429724, 0.2128401, 0.35821828, -0.2509771, -0.26594982, 0.18869537, -0.21725583, -0.35601154, -0.36929485, -0.29925507, -0.47262815, -0.041473743, 0.10217856, 0.062293913, -0.15322512, 0.08956682, -0.35481754, 0.058380894, 0.5370905, 0.40207297, 0.10658187, -0.31264502, 0.22212799, -0.05873761, 0.28276542, 0.04365597, 0.23748645, 0.29086804, 0.10375105, 0.32179505, -0.10878695, 0.17493275, 0.10128974, -0.046946246, -0.33823404, 0.33285227, -0.054822538, 0.25945452, 0.07178426, -0.14386761]


sql_columns = ["track_name", "track_artist", "track_album_name", "lyrics", "playlist_genre", "playlist_subgenre"]
columns = ["track_name", "artist_name", "album_name", "lyrics", "genre", "subgenre"]
limits = [10, 20, 30]
databases = ["document", "sql_single_table", "sql", "vector"]
benchmarks = {
    "BM1": { # Benchmark 1: Search for a single word in a single column
        "query": "love",
        "is_array": False,
        "columns": columns

    },
    "BM2": { # Benchmark 2: Search for a single word in all columns
        "query": ["Love", "Cake", "Fame"],
        "is_array": True,
        "columns": columns
    },
    "BM3": { # Benchmark 3: Search for sentence in all columns
        "query": "What is love",
        "is_array": False,
        "columns": columns
    },
    "BM4": { # Benchmark 4: Search in single column
        "query": "love",
        "is_array": False,
        "columns": ["track_name"]
    },
    "BM5": { # Benchmark 5: Search for song with vector
        "query": example_vector,
        "is_array": False,
        "columns": columns
        }
}

def aggregate_query_time(func, n=100):
    '''
    Aggregate the query time for a function
    '''
    total_time = 0
    for i in range(n):
        time = measure(func)
        total_time += time
        # print (f"Query {i}/{n} took {time} seconds")
    return total_time / n

def measure(func):
    '''
    Measure execution time of a function
    '''
    start = timer()

    func()

    end = timer()
    return end - start

def executeSql(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def run_benchmark(query, benchmark_id, database, limit):
    query_time = aggregate_query_time(lambda: query.do())
    result = query.do()

    count = len(result["data"]["Get"]["Track"])
    result = get_track_names(sorted([t["track_name"] for t in result["data"]["Get"]["Track"]])[:10])
    df = pd.DataFrame({"id": benchmark_id, "database": database, "avg_query_time": query_time, "count_result": count, "result": result, "limit": limit}, index=[0])
    print(f"- Time for {database} database: {query_time}")
    return df

def run_benchmark_sql(q, benchmark_id, database, limit):
    try:
        cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='spotifyDataset')
        cursor = cnx.cursor()

        query_time = aggregate_query_time(func=(lambda: executeSql(cursor, query = q)))

        result = executeSql(cursor, q)

        cnx.close()

        count = len(result)
        result = get_track_names(sorted(t[0] for t in result)[:10])
        
        df = pd.DataFrame({"id": benchmark_id, "database": database, "avg_query_time": query_time, "count_result": count, "result": result , "limit": limit}, index=[0])
        print(f"- Time for {database} database: {query_time}")
        return df
        
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

def main(args):
    '''
    Benchmark weaviate vs. SQL similiarity query performance
    Query the databases and measure the execution time
    for Vector, Document and SQL databases.
    Run benchmark 100x and take the average 
    We evaluate the quality of results ourselves
    '''

    # init dbs
    weaviate_client = init_client()

    df = pd.DataFrame(columns=["id", "database", "avg_query_time", "count_result","result", "limit"])

    # query benchmarks
    for key, benchmark in benchmarks.items():
        query = benchmark["query"]
        is_array = benchmark["is_array"]
        columns = benchmark["columns"]

        for limit in limits:
            print("-----------------------------------------------------------") 
            print(f"{key} with limit {limit}")
            print("-----------------------------------------------------------") 

            for database in databases:
                print(f"Measuring benckmark for {database} database ...") 
                if database == "vector":
                    if key == 'BM5':
                        q = ( 
                            weaviate_client.query
                            .get("Track", ["track_name"])
                            .with_near_vector({ "vector": example_vector})
                        )
                    else: 
                        nearText = {
                            "concepts": query if is_array else [query],
                        } 
                        q = ( 
                            weaviate_client.query
                            .get("Track", ["track_name"])
                            .with_near_text(nearText)
                        )
                    if limit > 1:
                        q = q.with_limit(limit)
                    result = run_benchmark(query=q, benchmark_id=key, database=database, limit=limit)
                elif database == "document":
                    if key == 'BM5':
                        continue
                    withFilter = {
                        "operator": "Or",
                        "operands": get_operands(query, columns=columns, is_array=is_array)
                    }
                    q = ( 
                        weaviate_client.query
                        .get("Track", ["track_name"])
                        .with_where(withFilter)
                    )
                    if limit > 1:
                        q = q.with_limit(limit)
                    result = run_benchmark(query=q, benchmark_id=key, database=database, limit=limit)
                elif database == "sql":
                    if key == 'BM5':
                        continue
                    q = build_sql_query(query, columns = (columns if key=='BM4' else sql_columns), limit=limit, is_array=is_array)
                    result = run_benchmark_sql(q, benchmark_id=key, database=database, limit=limit)
                elif database == "sql_single_table":
                    q = build_sql_query(query, columns = (columns if key=='BM4' else sql_columns), limit=limit, is_array=is_array, is_singelTable=True)
                    result = run_benchmark_sql(q, benchmark_id=key, database=database, limit=limit)

                df = pd.concat([df, result], ignore_index=True)
            print("-----------------------------------------------------------") 
    save_results(df)

    # cursor.close()
    # cnx.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Benchmark weaviate vs. SQL vs. Document query performance")
    args = parser.parse_args()

    main(args)
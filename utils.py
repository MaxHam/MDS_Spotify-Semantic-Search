from datetime import datetime
import pandas as pd


columns = ["track_name", "artist_name", "album_name", "lyrics", "genre", "subgenre"]
sql_columns = ["track_name", "track_artist", "track_album_name", "lyrics", "playlist_genre", "playlist_subgenre"]

def get_track_names(result):
    return ", ".join(result)

def get_operands(query, columns=columns, is_array=False):
    if is_array:
        return [
            {
                "operator": "And",
                "operands": [
                    {
                        "path": [c],
                        "operator": "Like",
                        "valueText": f'*{text}*'
                    }
                for text in query]
            } 
            for c in columns]
    else:
        return [
            {
                "path": [c],
                "operator": "Like",
                "valueText": f'*{query}*'
            }
            for c in columns]
    
def save_results(results):
    '''
    Save the results to a .csv file
    '''
    df = pd.DataFrame(results)
    df.to_csv("benchmark_results/benchmark_results" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv")


def add_limit (limit):
    if limit > 0:
        return f"LIMIT {limit}"
    else:
        return ""
    

    
def build_sql_query(query, columns, limit, is_array=False, is_singelTable=False):
    mul_query = []
    for column in columns:
        if is_array:
            tmp =  [ f"{column} LIKE '%{text}%' " for text in query]
            q = " AND ".join(tmp)
        else:
            q =  f"{column} LIKE '%{query}%' "
        mul_query.append(q)
    where = " OR ".join(mul_query)

    innerjoin = """
    inner join artist on track.artist_id = artist.id
inner join album on track.track_album_id = album.track_album_id
inner join playlist on track.playlist_id = playlist.playlist_id"""

    final_sql = f"""SELECT track_name
                FROM {"music_data" if is_singelTable else "track"}{"" if is_singelTable else innerjoin}
                WHERE {where}
                {add_limit(limit)};"""
    return final_sql
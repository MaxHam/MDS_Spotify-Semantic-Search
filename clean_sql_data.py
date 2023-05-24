import pandas as pd
import json
import re

def rpQuote(text):
    return filter_out_non_utf16_chars(text.replace("'", "''"))

def rpDate(text):
    sql_date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(sql_date_pattern, text):
        return "'" + text + "'"
    else:
        return "null"

def filter_out_non_utf16_chars(s):
    return s#s.encode('utf8', 'ignore').decode('utf8')

def main(args):
    # import csv
    df = pd.read_csv(args.import_file)
    # check for duplicate track_id
    # print(f"Before Cleaning: Number of duplicate track_id: {df.duplicated(subset='track_id').sum()}")
    # clean data
    df = df.dropna()
    # drop duplicate track_id
    df = df.drop_duplicates(subset="track_id")
    df = df.reset_index(drop=True)

    df = df.reset_index()  # make sure indexes pair with number of rows



    sql = """
CREATE DATABASE IF NOT EXISTS spotifyDataset;
USE spotifyDataset;
    
DROP TABLE IF EXISTS music_data;
    
CREATE TABLE music_data (
    id INT PRIMARY KEY,
    track_id VARCHAR(255) ,
    track_name VARCHAR(255) CHARACTER SET utf16,
    track_artist VARCHAR(255),
    lyrics MEDIUMTEXT CHARACTER SET utf16,
    track_popularity INT,
    track_album_id VARCHAR(255),
    track_album_name VARCHAR(255) CHARACTER SET utf16,
    track_album_release_date DATE,
    playlist_name VARCHAR(511) CHARACTER SET utf16,
    playlist_id VARCHAR(255),
    playlist_genre VARCHAR(255),
    playlist_subgenre VARCHAR(255),
    danceability FLOAT,
    energy FLOAT,
    musicKey INT,
    loudness FLOAT,
    mode INT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    duration_ms INT,
    language VARCHAR(255)
);


INSERT INTO music_data (
    id,
    track_id, 
    track_name, 
    track_artist, 
    lyrics, 
    track_popularity, 
    track_album_id, 
    track_album_name, 
    track_album_release_date, 
    playlist_name, 
    playlist_id, 
    playlist_genre, 
    playlist_subgenre, 
    danceability, 
    energy, 
    musicKey, 
    loudness, 
    mode, 
    speechiness, 
    acousticness, 
    instrumentalness, 
    liveness, 
    valence, 
    tempo, 
    duration_ms, 
    language
) 
VALUES 
"""

    #df = df.head(10)

    for index, row in df.iterrows():
        #id,track_id,track_name,track_artist,lyrics,track_popularity,track_album_id,track_album_name,track_album_release_date,playlist_name,playlist_id,playlist_genre,playlist_subgenre,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,language
        if(row[1] != "3N29lMZHMKTVGXUN5aqzl5" and row[1] != "5lFDtgWsjRJu8fPOAyJIAK"):
            sql += f"({row[0]},'{rpQuote(row[1])}','{rpQuote(row[2])}','{rpQuote(row[3])}','{rpQuote(row[4])}',{row[5]},'{rpQuote(row[6])}','{rpQuote(row[7])}',{rpDate(row[8])},'{rpQuote(row[9])}','{rpQuote(row[10])}','{rpQuote(row[11])}','{rpQuote(row[12])}',{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},{row[18]},{row[19]},{row[20]},{row[21]},{row[22]},{row[23]},{row[24]},'{rpQuote(row[25])}'),\n"
        if(index % 100 == 0):
            print(index)

    sql = sql[:-2]
    sql += """;"""

    # save json file
    with open("data/spotify_songs.sql", "w") as f:
        f.write(sql)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Clean data for weaviate import.")
    parser.add_argument("-i", "--import_file",
                        default="data/spotify_songs.csv", type=str)
    args = parser.parse_args()

    main(args)
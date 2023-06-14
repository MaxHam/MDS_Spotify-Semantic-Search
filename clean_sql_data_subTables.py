import pandas as pd
import json
import re

def rpQuote(text):
    return text.replace("'", "''").replace(";","")

def rpDate(text):
    sql_date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(sql_date_pattern, text):
        return "'" + text + "'"
    else:
        return "null"


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



    sql = """CREATE DATABASE IF NOT EXISTS spotifyDataset;
USE spotifyDataset;
DROP TABLE IF EXISTS track;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;
DROP VIEW IF EXISTS music_data_view;

CREATE TABLE artist
(
    id INT PRIMARY KEY,
    track_artist VARCHAR(255)
);

CREATE TABLE album
(
    track_album_id VARCHAR(22) PRIMARY KEY,
    track_album_name VARCHAR(255) CHARACTER SET utf16,
    track_album_release_date DATE,
    INDEX track_album_id_index (track_album_id)
);

CREATE TABLE playlist
(
    playlist_id VARCHAR(22) PRIMARY KEY,
    playlist_name VARCHAR(511) CHARACTER SET utf16,
    playlist_genre VARCHAR(255),
    playlist_subgenre VARCHAR(255),
    INDEX playlist_id_index (playlist_id)
);

CREATE TABLE track (
    track_id VARCHAR(22) PRIMARY KEY,
    track_name VARCHAR(255) CHARACTER SET utf16,
    lyrics MEDIUMTEXT CHARACTER SET utf16,
    track_popularity INT,
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
    language VARCHAR(255),
    artist_id INT,
    track_album_id VARCHAR(22),
    playlist_id VARCHAR(22),
    FOREIGN KEY (artist_id) REFERENCES artist(id),
    FOREIGN KEY (track_album_id) REFERENCES album(track_album_id),
    FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
    INDEX(track_album_id),
    INDEX(playlist_id)
);
 
"""

    
#    df = df.head(10)



    #artist insert
    sql_instert = """INSERT INTO artist (id, track_artist) VALUES """

    artist = {}
    
    index = 0

    #add artist
    for index, row in df.iterrows():
        #track_artist
        if(row[1] != "3N29lMZHMKTVGXUN5aqzl5" and row[1] != "5lFDtgWsjRJu8fPOAyJIAK" and row[3] not in artist):
            sql += sql_instert + f"({index},'{rpQuote(row[3])}');\n"
            artist[row[3]] = index
            index += 1
        if(index % 100 == 0):
            print(index)

    #album insert
    sql_instert = """INSERT INTO album (track_album_id,track_album_name,track_album_release_date) VALUES """

    albums = []
    
    #add album
    for index, row in df.iterrows():
        #track_album_id,track_album_name,track_album_release_date
        if(row[1] != "3N29lMZHMKTVGXUN5aqzl5" and row[1] != "5lFDtgWsjRJu8fPOAyJIAK" and not albums.__contains__(row[6])):
            sql += sql_instert + f"('{rpQuote(row[6])}','{rpQuote(row[7])}',{rpDate(row[8])});\n"
            albums.append(row[6])
        if(index % 100 == 0):
            print(index)

    #playlist insert
    sql_instert = """INSERT INTO playlist (playlist_name,playlist_id,playlist_genre,playlist_subgenre) VALUES """
    
    playlists = []

    #add playlist
    for index, row in df.iterrows():
        #playlist_name,playlist_id,playlist_genre,playlist_subgenre
        if(row[1] != "3N29lMZHMKTVGXUN5aqzl5" and row[1] != "5lFDtgWsjRJu8fPOAyJIAK" and not playlists.__contains__(row[10])):
            sql += sql_instert + f"('{rpQuote(row[9])}','{rpQuote(row[10])}','{rpQuote(row[11])}','{rpQuote(row[12])}');\n"
            playlists.append(row[10])
        if(index % 100 == 0):
            print(index)

    sql_instert = """INSERT INTO track (track_id,track_name,lyrics,track_popularity,danceability,energy,musicKey,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,language,artist_id,track_album_id,playlist_id) VALUES """


    #add tracks
    for index, row in df.iterrows():
        #track_id,track_name,lyrics,track_popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,language,track_album_id,playlist_id
        if(row[1] != "3N29lMZHMKTVGXUN5aqzl5" and row[1] != "5lFDtgWsjRJu8fPOAyJIAK"):
            sql += sql_instert + f"('{rpQuote(row[1])}','{rpQuote(row[2])}','{rpQuote(row[4])}',{row[5]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},{row[18]},{row[19]},{row[20]},{row[21]},{row[22]},{row[23]},{row[24]},'{rpQuote(row[25])}',{artist.get(row[3])},'{rpQuote(row[6])}','{rpQuote(row[10])}');\n"
        if(index % 100 == 0):
            print(index)

    sql = sql[:-2]
    sql += """;"""

    sql += """CREATE VIEW music_data_view AS
SELECT track_id,track_name,track_artist,lyrics,track_popularity,track_album_name,track_album_release_date,playlist_name,playlist_genre,playlist_subgenre,danceability,energy,track.musicKey,loudness,track.mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,language
FROM track
JOIN playlist p ON p.playlist_id = track.playlist_id
JOIN album a ON a.track_album_id = track.track_album_id
JOIN artist a2 ON a2.id = track.artist_id;"""


    # save json file
    with open("data/spotify_songs.sql", "w", encoding="utf-16") as f:
        f.write(sql)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Clean data for weaviate import.")
    parser.add_argument("-i", "--import_file",
                        default="data/spotify_songs.csv", type=str)
    args = parser.parse_args()

    main(args)
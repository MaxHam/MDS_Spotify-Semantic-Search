import pandas as pd
import json
import weaviate

def main(args):
    # import csv
    df = pd.read_csv(args.import_file)
    # clean data
    df = df.dropna()
    # drop duplicate track_id
    df = df.drop_duplicates(subset="track_id")
    df = df.reset_index(drop=True)
    # convert to json
    df_json = df.to_json(orient="records")
    # save json file
    with open("data/spotify_songs.json", "w") as f:
        f.write(df_json)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Clean data for weaviate import.")
    parser.add_argument("-i", "--import_file",
                        default="data/spotify_songs.csv", type=str)
    args = parser.parse_args()

    main(args)

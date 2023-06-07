import json
from weaviate_import import init_client


def query(client):
    where_filter = {
        "path": ["popularity"],
        "operator": "GreaterThan",
        "valueNumber": "80"
    }
    nearText = {
        "concepts": ["Galileo"],
    }  

    result = ( 
        client.query
        .get("Track", ["track_name"])
        # .with_where(where_filter)
        .with_near_text(nearText)
        .with_limit(2)
        .do()
    )

    print(json.dumps(result, indent=4))

def ask(client):
    ask = {
        "question": "Ariana Grande?",
        "properties": ["name"],
    }

    result = (
        client.query
        .get("Track", ["name", "_additional {answer {hasAnswer certainty property result startPosition endPosition} }"])
        .with_ask(ask)
        .with_limit(1)
        .do()
        )
    print(json.dumps(result, indent=4))

def main(args):
    client = init_client()
    # query(client)
    # ask(client)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Benchmark weaviate vs. SQL query performance")
    args = parser.parse_args()

    main(args)
import os

from elasticsearch import Elasticsearch

client = Elasticsearch(
    os.getenv("ELASTIC_HOST"),
    basic_auth=(
        os.getenv("ELASTIC_USER"),
        os.getenv("ELASTIC_PASSWORD"),
    )
)


def vector_search(query_embedding, top_k=5):

    response = client.search(
        index=os.getenv("INDEX_NAME"),
        knn={
            "field": "embedding",
            "query_vector": query_embedding,
            "k": top_k,
            "num_candidates": 50,
        },
    )

    docs = []

    for hit in response["hits"]["hits"]:
        docs.append(hit["_source"]["content"])

    return docs
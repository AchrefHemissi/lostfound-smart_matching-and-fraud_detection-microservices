from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "lostfound_embeddings"

def qdrant_store(post_id: str, embedding, metadata):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=post_id, vector=embedding, payload=metadata)]
    )

def qdrant_search(post_id: str):
    original = client.retrieve(collection_name=COLLECTION_NAME, ids=[post_id])
    if not original:
        return []

    embedding = original[0].vector
    metadata = original[0].payload

    # Preselection filter (example: same city and category)
    city = metadata.get("city")
    category = metadata.get("category")

    # Build Qdrant filter condition
    filter = {
        "must": [
            {"key": "city", "match": {"value": city}},
            {"key": "category", "match": {"value": category}},
        ]
    }

    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embedding,
        top=5,
        query_filter=filter
    )
    return [hit.payload for hit in hits]


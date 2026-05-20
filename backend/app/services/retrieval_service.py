from app.services.embedding_service import generate_embedding
from app.services.vector_store import collection


def search_similar_chunks(query: str, n_results: int = 3):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    chunks = results["documents"][0]

    return chunks
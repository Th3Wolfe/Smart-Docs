from app.services.embedding_service import generate_embedding
from app.services.vector_store import collection


def search_similar_chunks(query: str, document_id: str = None, n_results: int = 8):

    # 1. gerar embedding da pergunta
    query_embedding = generate_embedding(query)

    # 2. busca no ChromaDB (com ou sem filtro de documento)
    if document_id:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where={"document_id": document_id}
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

    # 3. validação de segurança (caso não retorne nada)
    if not results["documents"] or len(results["documents"][0]) == 0:
        return []

    # 4. retorna chunks mais relevantes
    return results["documents"][0]
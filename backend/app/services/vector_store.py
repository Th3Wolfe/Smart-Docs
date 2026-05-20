import chromadb
from app.services.embedding_service import generate_embedding

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="smartdocs"
)


def add_chunks(document_id: str, chunks: list):

    for i, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            ids=[f"{document_id}_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "document_id": document_id,
                "chunk_index": i
            }]
        )
from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
from typing import Optional
from app.services.ollama_service import generate_response
from app.services.document_service import extract_text
from app.services.chunk_service import create_chunks
from app.services.retrieval_service import search_similar_chunks
from app.services.vector_store import add_chunks
from app.services.vector_store import collection

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(
    title="SmartDocs API",
    version="1.0.0"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "SmartDocs API is running"
    }


@app.get("/chat")
def chat(prompt: str):

    response = generate_response(prompt)

    return {
        "response": response
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(str(file_path))
    chunks = create_chunks(extracted_text)

    document_id = file.filename  # (ou uuid depois)

    add_chunks(document_id, chunks)

    return {
        "filename": file.filename,
        "document_id": document_id,
        "total_chunks": len(chunks),
        "status": "indexado no ChromaDB com sucesso"
    }

@app.get("/ask")
def ask(query: str, document_id: str = None):
    
    if document_id:
        chunks = search_similar_chunks(query, document_id)
    else:
        chunks = search_similar_chunks(query, None)

    context = "\n\n".join(chunks)

    prompt = f"""
Você é um assistente que responde SOMENTE com base no contexto abaixo.

Se não tiver informação no contexto, diga que não encontrou.

Contexto:
{context}

Pergunta:
{query}

Responda de forma clara e objetiva.
"""

    response = generate_response(prompt)

    return {
        "query": query,
        "answer": response,
        "context_used": chunks
    }

@app.get("/documents")
def list_documents():

    data = collection.get()

    if not data["metadatas"]:
        return {"documents": []}

    documents = list({
        meta["document_id"]
        for meta in data["metadatas"]
        if "document_id" in meta
    })

    return {
        "documents": documents
    }
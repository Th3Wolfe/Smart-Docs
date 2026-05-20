from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
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

    # 1. extrair texto
    extracted_text = extract_text(str(file_path))

    # 2. criar chunks
    chunks = create_chunks(extracted_text)

    # 3. salvar no ChromaDB (FALTAVA ISSO)
    document_id = file.filename
    add_chunks(document_id, chunks)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "status": "indexado no ChromaDB com sucesso"
    }

@app.get("/ask")
def ask(query: str):

    chunks = search_similar_chunks(query)

    context = "\n\n".join(chunks)

    prompt = f"""
Você é um assistente que responde com base em documentos.

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

@app.get("/debug/chroma")
def debug_chroma():

    data = collection.get()

    return {
        "total_ids": len(data["ids"]) if data["ids"] else 0,
        "ids": data["ids"],
        "documents_preview": data["documents"][:3] if data["documents"] else []
    }
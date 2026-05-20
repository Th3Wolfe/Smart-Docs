from fastapi import FastAPI, UploadFile, File
from app.services.ollama_service import generate_response
from app.services.document_service import extract_text
from app.services.chunk_service import create_chunks

import shutil
from pathlib import Path

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

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "first_chunk": chunks[0]
    }
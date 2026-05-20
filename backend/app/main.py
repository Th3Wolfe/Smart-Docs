from fastapi import FastAPI
from app.services.ollama_service import generate_response

app = FastAPI(
    title="SmartDocs API",
    version="1.0.0"
)


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
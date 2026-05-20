from fastapi import FastAPI

app = FastAPI(
    title="SmartDocs API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SmartDocs API is running"
    }
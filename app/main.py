import logging
from fastapi import FastAPI, HTTPException

from app import classify_headline, ModelRequest, ModelResponse

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/classify")
async def classify_headline_endpoint(request: ModelRequest):
    logging.info(f"Received request to classify -> {request.headline}")
    try:
        response = classify_headline(request.headline)
        logging.info(f"Model Response -> {response['label']} with confidence {response['score']}")
        return ModelResponse(sentiment=response['label'], confidence=response['score'])
    except Exception as e:
        raise HTTPException(status_code=500, detail="Classification failed")
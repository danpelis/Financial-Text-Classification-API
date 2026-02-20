from transformers import pipeline
from app.config import MODEL_NAME

pipeline = pipeline("text-classification", model=MODEL_NAME)

def classify_headline(headline:str) -> str:
    result = pipeline(headline)
    return result[0]

if __name__ == "__main__":
    headline = "The stock market is crashing"
    result = classify_headline(headline)
    print(result)
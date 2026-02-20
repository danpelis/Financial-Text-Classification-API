from pydantic import BaseModel, Field
from app import MAX_LENGTH

class ModelRequest(BaseModel):
    headline: str = Field(min_length=1, max_length=MAX_LENGTH)

class ModelResponse(BaseModel):
    sentiment: str
    confidence: float
from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text to analyze")

class ClassificationResponse(BaseModel):
    category: str
    confidence: float
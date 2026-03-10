from pydantic import BaseModel

class ClassificationResponse(BaseModel):
    category: str
    confidence: float

class SummaryResponse(BaseModel):
    summary: str
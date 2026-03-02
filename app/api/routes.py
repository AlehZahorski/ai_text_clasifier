from fastapi import APIRouter
from app.schemas.request_response import TextRequest, ClassificationResponse
from app.services.text_service import classify_text

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/classify", response_model=ClassificationResponse)
def classify(request: TextRequest):
    return classify_text(request.text)
from fastapi import APIRouter
import logging
from app.schemas.request import TextRequest
from app.schemas.response import ClassificationResponse
from app.schemas.response import SummaryResponse
from app.services.summarizer import summarize_text
from app.services.text_service import classify_text

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/classify", response_model=ClassificationResponse)
def classify(request: TextRequest):

    logger.info(f"/classify request: {request.text}")

    return classify_text(request.text)

@router.post("/summarize", response_model=SummaryResponse)
def summarize(request: TextRequest):

    logger.info(f"/summarize request: {request.text}")

    return summarize_text(request.text)
import time
import logging
from app.services.prompt_builder import build_classification_prompt
from app.schemas.response import ClassificationResponse
from app.services.llm_client import ask_llm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def classify_text(text: str):

    prompt = build_classification_prompt(text)

    start_time = time.time()

    parsed = ask_llm(
        prompt,
        system_role="You are a text classification system."
    )

    latency = time.time() - start_time
    logger.info(f"Classification latency: {latency:.3f}s")

    validated = ClassificationResponse(**parsed)

    return validated.model_dump()
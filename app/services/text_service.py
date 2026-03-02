import json
from openai import OpenAI
import time
import logging
from openai import APIError, RateLimitError, APITimeoutError
from fastapi import HTTPException
from app.core.config import settings
from app.services.prompt_builder import build_classification_prompt
from app.schemas.request_response import ClassificationResponse

client = OpenAI(api_key=settings.OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

start_time = time.time()
def classify_text(text: str) -> dict:
    prompt = build_classification_prompt(text)

    try:
        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a text classification system."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            timeout=settings.LLM_TIMEOUT,
            response_format={"type": "json_object"}
        )

    except APITimeoutError:
        raise HTTPException(status_code=503, detail="LLM request timed out")

    except RateLimitError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    except APIError:
        raise HTTPException(status_code=502, detail="OpenAI API error")

    content = response.choices[0].message.content

    try:
        parsed = json.loads(content)

        latency = time.time() - start_time
        logger.info(f"Classification latency: {latency:.3f}s")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Model returned invalid JSON")

    try:
        validated = ClassificationResponse(**parsed)
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid model response structure")

    return validated.model_dump()
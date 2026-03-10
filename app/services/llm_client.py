import json
import time
from openai import OpenAI
from openai import APIError, RateLimitError, APITimeoutError
from fastapi import HTTPException
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_llm(prompt: str, system_role: str, retries: int = 3):

    for attempt in range(retries):

        try:
            response = client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                timeout=settings.LLM_TIMEOUT,
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content
            return json.loads(content)

        except (APITimeoutError, RateLimitError, APIError):

            if attempt == retries - 1:
                raise HTTPException(status_code=502, detail="LLM request failed after retries")

            time.sleep(1)

        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Model returned invalid JSON")
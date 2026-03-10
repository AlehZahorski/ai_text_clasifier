import json
from openai import OpenAI
from openai import APIError, RateLimitError, APITimeoutError
from fastapi import HTTPException
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_llm(prompt: str, system_role: str):

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

    except APITimeoutError:
        raise HTTPException(status_code=503, detail="LLM request timed out")

    except RateLimitError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    except APIError:
        raise HTTPException(status_code=502, detail="OpenAI API error")

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Model returned invalid JSON")
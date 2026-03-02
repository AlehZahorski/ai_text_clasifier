import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    LLM_TIMEOUT: int = int(os.getenv("LLM_TIMEOUT", 30))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()

if not settings.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

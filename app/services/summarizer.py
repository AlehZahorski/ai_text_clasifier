from app.services.llm_client import ask_llm
from app.services.prompt_builder import build_summary_prompt
from app.schemas.response import SummaryResponse


def summarize_text(text: str):

    prompt = build_summary_prompt(text)

    parsed = ask_llm(
        prompt,
        system_role="You are a system that summarizes customer messages."
    )

    validated = SummaryResponse(**parsed)

    return validated.model_dump()
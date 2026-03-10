from app.services.text_service import ask_llm
from app.services.prompt_builder import build_summary_prompt


def summarize_text(text: str):

    prompt = build_summary_prompt(text)

    return ask_llm(prompt, 'You are a system commarizer role.')
def build_classification_prompt(text: str) -> str:
    return f"""
Classify the following message into one of these categories:
- complaint
- question
- praise
- other

Return ONLY a valid JSON object in this format:
{{
    "category": "category_name",
    "confidence": 0.0
}}

Message:
"{text}"
"""
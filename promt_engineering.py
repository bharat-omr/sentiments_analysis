def build_prompt(review: str) -> str:
    return f"""
You are a product review assistant. Given a review, identify the sentiment 
(Positive/Negative/Neutral), extract key points, and suggest improvements to make the review 
more detailed and helpful.

Your JSON must follow this structure:

{{
  "sentiment": "Positive/Negative/Neutral",
  "key_phrases": ["..."],
  "suggestions": "..."
}}

DO NOT include explanations or anything else—just valid JSON.

Review: "{review}"
"""

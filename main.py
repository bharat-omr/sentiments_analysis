from fastapi import FastAPI, HTTPException
from model import ReviewRequest, ReviewResponse, ReviewInDB
from promt_engineering import build_prompt
from llm_gemini import ask_gemini
from database import review_collection
import json
import re

app = FastAPI()

def extract_json(text: str) -> str:
    text = text.strip().strip("`")
    match = re.search(r'\{[\s\S]*\}', text)
    if match:
        return match.group(0)
    raise ValueError("Could not extract JSON from response.")

@app.post("/analyze-review", response_model=ReviewResponse)
async def analyze_review(data: ReviewRequest):
    try:
        prompt = build_prompt(data.review)
        raw_response = ask_gemini(prompt)
        json_text = extract_json(raw_response)
        response_json = json.loads(json_text)

        review_doc = {
            "review_text": data.review,
            "sentiment": response_json.get("sentiment", "Unknown"),
            "key_phrases": response_json.get("key_phrases", []),
            "suggestions": response_json.get("suggestions", ""),
        }

        # Insert into MongoDB
        await review_collection.insert_one(review_doc)

        return ReviewResponse(
            sentiment=review_doc["sentiment"],
            key_phrases=review_doc["key_phrases"],
            suggestions=review_doc["suggestions"]
        )
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="LLM response could not be parsed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=list[ReviewInDB])
async def get_history():
    reviews_cursor = review_collection.find()
    reviews = []
    async for review in reviews_cursor:
        reviews.append(
            ReviewInDB(
                review_text=review.get("review_text", ""),
                sentiment=review.get("sentiment", ""),
                key_phrases=review.get("key_phrases", []),
                suggestions=review.get("suggestions", "")
            )
        )
    return reviews

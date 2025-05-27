from pydantic import BaseModel
from typing import List

class ReviewRequest(BaseModel):
    review: str

class ReviewResponse(BaseModel):
    sentiment: str
    key_phrases: List[str]
    suggestions: str

class ReviewInDB(ReviewResponse):
    review_text: str

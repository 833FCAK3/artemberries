from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException

from models import ReviewsDTO


fake_reviews_db = [
    {
        "_id": "65fabc1234567890abcdef12",
        "product_id": 1,
        "user_id": 1,
        "rating": 5,
        "comment": "Wunderbar",
        "created_at": datetime.now(),
    }
]

reviews = APIRouter()


@reviews.get("/reviews", response_model=List[ReviewsDTO])
async def get_reviews():
    return fake_reviews_db


@reviews.get("/reviews/{product_id}", response_model=List[ReviewsDTO])
async def get_review(product_id: int):
    data = []
    for review in fake_reviews_db:
        if review["product_id"] == product_id:
            data.append(review)
    return data


@reviews.post("/reviews", status_code=201)
async def add_review(payload: ReviewsDTO):
    review = payload.model_dump(by_alias=True, exclude={"id"})
    fake_reviews_db.append(review)
    return review


@reviews.delete("/{product_id}")
async def delete_review(product_id: int):
    reviews_length = len(fake_reviews_db)
    if 0 <= product_id <= reviews_length:
        for review in fake_reviews_db[:]:
            if review["product_id"] == product_id:
                fake_reviews_db.remove(review)
        return None
    raise HTTPException(status_code=404, detail="Reviews with given id not found")

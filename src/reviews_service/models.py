from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


# class PyObjectId(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid ObjectId")
#         return str(v)


class ReviewsDTO(BaseModel):
    # id: Optional[PyObjectId] = Field(alias="_id", default=None)
    _id: Optional[str]
    product_id: int | str
    user_id: int | str
    rating: int
    comment: str
    created_at: datetime

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        extra = "allow"

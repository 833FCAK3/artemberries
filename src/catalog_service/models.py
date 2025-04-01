from typing import List

from pydantic import BaseModel


class Products(BaseModel):
    id: int
    name: str
    price: float
    category_id: int


class Categories(BaseModel):
    id: int
    name: str

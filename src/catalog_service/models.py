from typing import List

from pydantic import BaseModel


class ProductsDTO(BaseModel):
    id: int
    name: str
    price: float
    category_id: int


class CategoriesDTO(BaseModel):
    id: int
    name: str

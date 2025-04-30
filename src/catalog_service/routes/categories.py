from typing import List

from fastapi import APIRouter, HTTPException

from catalog_service.models import CategoriesDTO


fake_categories_db = [
    {
        "id": 1,
        "name": "GPU",
    }
]

category = APIRouter()


@category.get("/categories", response_model=List[CategoriesDTO])
async def get_categories():
    return fake_categories_db


@category.get("/categories/{category_id}", response_model=CategoriesDTO)
async def get_category(category_id: int):
    category = None
    for category_ in fake_categories_db:
        if category_["id"] == category_id:
            category = category_
    return category


@category.post("/categories", status_code=201)
async def add_category(payload: CategoriesDTO):
    category = payload.model_dump()
    fake_categories_db.append(category)
    return {"id_": category["id"]}


@category.put("/categories/{category_id}")
async def update_category(category_id: int, payload: CategoriesDTO):
    category = payload.model_dump()
    categories_length = len(fake_categories_db)
    if 0 <= category_id <= categories_length:
        fake_categories_db[category_id - 1] = category
        return None
    raise HTTPException(status_code=404, detail="Category with given id not found")


@category.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    categories_length = len(fake_categories_db)
    if 0 <= category_id <= categories_length:
        del fake_categories_db[category_id - 1]
        return None
    raise HTTPException(status_code=404, detail="Category with given id not found")

from typing import List

from fastapi import APIRouter, HTTPException

from src.catalog_service.models import CategoriesDTO, ProductsDTO


fake_products_db = [
    {
        "id": 1,
        "name": "RTX 4090",
        "price": 100,
        "category_id": 1,
    }
]

fake_categories_db = [
    {
        "id": 1,
        "name": "GPU",
    }
]

catalog = APIRouter()


@catalog.get("/products", response_model=List[ProductsDTO])
async def get_products():
    return fake_products_db


@catalog.get("/products/{product_id}", response_model=ProductsDTO)
async def get_product(product_id: int):
    data = None
    for product in fake_products_db:
        if product["id"] == product_id:
            data = product
    return data


@catalog.post("/products", status_code=201)
async def add_product(payload: ProductsDTO):
    product = payload.model_dump()
    fake_products_db.append(product)
    return {"id_": product["id"]}


@catalog.put("/products/{product_id}")
async def update_product(product_id: int, payload: ProductsDTO):  # Match route param name
    product = payload.model_dump()
    products_length = len(fake_products_db)

    if 0 <= product_id <= products_length:
        fake_products_db[product_id - 1] = product
        return None

    raise HTTPException(status_code=404, detail="Product with given ID not found")


@catalog.delete("/products/{product_id}")
async def delete_product(product_id: int):
    products_length = len(fake_products_db)
    if 0 <= product_id <= products_length:
        del fake_products_db[product_id - 1]
        return None
    raise HTTPException(status_code=404, detail="Products with given id not found")


@catalog.get("/categories", response_model=List[CategoriesDTO])
async def get_categories():
    return fake_categories_db


@catalog.get("/categories/{category_id}", response_model=CategoriesDTO)
async def get_category(category_id: int):
    category = None
    for category_ in fake_categories_db:
        if category_["id"] == category_id:
            category = category_
    return category


@catalog.post("/categories", status_code=201)
async def add_category(payload: CategoriesDTO):
    category = payload.model_dump()
    fake_categories_db.append(category)
    return {"id_": category["id"]}


@catalog.put("/categories/{category_id}")
async def update_category(category_id: int, payload: CategoriesDTO):
    category = payload.model_dump()
    categories_length = len(fake_categories_db)
    if 0 <= category_id <= categories_length:
        fake_categories_db[category_id - 1] = category
        return None
    raise HTTPException(status_code=404, detail="Category with given id not found")


@catalog.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    categories_length = len(fake_categories_db)
    if 0 <= category_id <= categories_length:
        del fake_categories_db[category_id - 1]
        return None
    raise HTTPException(status_code=404, detail="Category with given id not found")

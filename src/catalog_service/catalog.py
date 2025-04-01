from typing import List

from fastapi import APIRouter, Header, HTTPException

from src.catalog_service.models import Categories, Products


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


@catalog.get("/products", response_model=List[Products])
async def get_products():
    return fake_products_db


@catalog.get("/products/{product_id}", response_model=Products)
async def get_product(product_id: int):
    product = None
    for product_ in fake_products_db:
        if product_["id"] == product_id:
            product = product_
    return product


@catalog.post("/products", status_code=201)
async def add_product(payload: Products):
    product = payload.model_dump()
    fake_products_db.append(product)
    return {"id_": product["id"]}


@catalog.put("/products/{product_id}")
async def update_product(id: int, payload: Products):
    product = payload.model_dump()
    products_length = len(fake_products_db)
    if 0 <= id <= products_length:
        fake_products_db[id] = product
        return None
    raise HTTPException(status_code=404, detail="Products with given id not found")


@catalog.delete("/products/{product_id}")
async def delete_product(id: int):
    products_length = len(fake_products_db)
    if 0 <= id <= products_length:
        del fake_products_db[id]
        return None
    raise HTTPException(status_code=404, detail="Products with given id not found")

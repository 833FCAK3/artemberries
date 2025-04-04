from typing import List

from fastapi import APIRouter, HTTPException

from models import ProductsDTO


fake_products_db = [
    {
        "id": 1,
        "name": "RTX 4090",
        "price": 100,
        "category_id": 1,
    }
]


product = APIRouter()


@product.get("/products", response_model=List[ProductsDTO])
async def get_products():
    return fake_products_db


@product.get("/products/{product_id}", response_model=ProductsDTO)
async def get_product(product_id: int):
    data = None
    for product in fake_products_db:
        if product["id"] == product_id:
            data = product
    return data


@product.post("/products", status_code=201)
async def add_product(payload: ProductsDTO):
    product = payload.model_dump()
    fake_products_db.append(product)
    return {"id_": product["id"]}


@product.put("/products/{product_id}")
async def update_product(product_id: int, payload: ProductsDTO):  # Match route param name
    product = payload.model_dump()
    products_length = len(fake_products_db)

    if 0 <= product_id <= products_length:
        fake_products_db[product_id - 1] = product
        return None

    raise HTTPException(status_code=404, detail="Product with given ID not found")


@product.delete("/products/{product_id}")
async def delete_product(product_id: int):
    products_length = len(fake_products_db)
    if 0 <= product_id <= products_length:
        del fake_products_db[product_id - 1]
        return None
    raise HTTPException(status_code=404, detail="Products with given id not found")

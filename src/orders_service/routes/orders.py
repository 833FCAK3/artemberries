import json
from datetime import datetime
from typing import List

import httpx
from fastapi import APIRouter, HTTPException

from src.orders_service.models import OrderItemsDTO, OrdersDTO, OrderStatusType


fake_orders_db = [
    {
        "id": 1,
        "user_id": 1,
        "status": OrderStatusType.CREATED,
        "total_price": 500,
        "tracking_number": "123456789",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
]

fake_order_items_db = [
    {
        "id": 1,
        "order_id": 1,
        "product_id": 1,
        "quantity": 5,
        "price_at_moment": 100,
    }
]

orders = APIRouter()


@orders.get("/orders", response_model=List[OrdersDTO])
async def get_orders():
    return fake_orders_db


@orders.get("/order_items", response_model=List[OrderItemsDTO])
async def get_orderitems():
    return fake_order_items_db


@orders.get("/orders/{order_id}", response_model=OrdersDTO)
async def get_order(order_id: int):
    data = None
    for order in fake_orders_db:
        if order["id"] == order_id:
            data = order
    return data


@orders.post("/orders", status_code=201)
async def add_order(payload: OrderItemsDTO):
    order_items = payload.model_dump()
    price_at_moment = await get_current_price(order_items)
    order_items["price_at_moment"] = price_at_moment

    order = OrdersDTO(
        id=order_items["id"],
        user_id=order_items["id"],
        total_price=order_items["quantity"] * price_at_moment,
    ).model_dump()

    fake_orders_db.append(order)
    fake_order_items_db.append(order_items)
    return [order, order_items]


@orders.patch("/orders/{order_id}")
async def update_order(order_id: int, payload: OrdersDTO):
    order = payload.model_dump()
    orders_length = len(fake_orders_db)
    if 0 <= order_id <= orders_length:
        fake_orders_db[order_id - 1] = order
        return None
    raise HTTPException(status_code=404, detail="Orders with given id not found")


@orders.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    orders_length = len(fake_orders_db)
    if 0 <= order_id <= orders_length:
        del fake_orders_db[order_id - 1]
        return None
    raise HTTPException(status_code=404, detail="Orders with given id not found")


async def get_current_price(order_items: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/products/{order_items['product_id']}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Product not found")
        elif response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching product")
        product = response.json()

        return product["price"]

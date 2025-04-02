import enum
from datetime import datetime
from typing import List

from pydantic import BaseModel


class OrderStatusType(str, enum.Enum):
    CREATED = "CREATED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELED = "CANCELED"


class OrdersDTO(BaseModel):
    id: int
    user_id: int
    status: str = OrderStatusType.CREATED
    total_price: float
    tracking_number: str | None = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class OrderItemsDTO(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price_at_moment: float

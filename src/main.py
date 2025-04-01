from fastapi import FastAPI

from .catalog_service.routes.categories import category
from .catalog_service.routes.products import product
from .orders_service.routes.orders import orders
from .reviews_service.routes.reviews import reviews


app = FastAPI()

app.include_router(product)
app.include_router(category)
app.include_router(orders)
app.include_router(reviews)

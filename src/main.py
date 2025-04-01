from fastapi import FastAPI

from .catalog_service.catalog import catalog
from .orders_service.orders import orders
from .reviews_service.reviews import reviews


app = FastAPI()

app.include_router(catalog)
app.include_router(orders)
app.include_router(reviews)

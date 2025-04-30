from fastapi import FastAPI

from catalog_service.routes.categories import category
from catalog_service.routes.products import product


app = FastAPI()

app.include_router(product)
app.include_router(category)

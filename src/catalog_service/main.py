from fastapi import FastAPI

from routes.categories import category
from routes.products import product


app = FastAPI()

app.include_router(product)
app.include_router(category)

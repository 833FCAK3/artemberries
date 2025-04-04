from fastapi import FastAPI

from routes.orders import orders


app = FastAPI()

app.include_router(orders)

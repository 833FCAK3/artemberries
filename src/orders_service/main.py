from fastapi import FastAPI

from orders_service.routes.orders import orders


app = FastAPI()

app.include_router(orders)

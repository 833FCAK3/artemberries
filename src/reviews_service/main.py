from fastapi import FastAPI

from reviews_service.routes.reviews import reviews


app = FastAPI()

app.include_router(reviews)

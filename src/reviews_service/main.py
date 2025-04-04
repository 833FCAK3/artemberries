from fastapi import FastAPI

from routes.reviews import reviews


app = FastAPI()

app.include_router(reviews)

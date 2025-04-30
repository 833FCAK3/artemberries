from databases import Database
from pymongo import MongoClient
from sqlalchemy import ARRAY, Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import settings


POSTGRES_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:5432/{settings.POSTGRES_DB}"

engine = create_engine(POSTGRES_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


PYMONGO_MONGO_URL = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"

mongo_client = MongoClient(PYMONGO_MONGO_URL)
mongo_db = mongo_client[settings.MONGO_DB]


def get_mongo_db():
    mongo_db = mongo_client[settings.MONGO_DB]
    return mongo_db

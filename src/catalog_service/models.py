import uuid
from typing import List

from pydantic import BaseModel
from sqlalchemy import ARRAY, ForeignKey, Integer, MetaData, Numeric, String, Table, create_engine
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from package.models import Column


class Products(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    price = Column(Numeric(10, 2))
    category_id = Column(ForeignKey("categories.id"))


class Categories(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)


class ProductsDTO(BaseModel):
    id: int
    name: str
    price: float
    category_id: int


class CategoriesDTO(BaseModel):
    id: int
    name: str

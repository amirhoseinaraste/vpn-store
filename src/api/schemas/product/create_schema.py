# import necessary packages
from pydantic import BaseModel
from typing import Optional

class CreateProduct(BaseModel):
    name: str
    category: str
    volume: int
    price: int
    duration: int

class responseCreateProductSchema(BaseModel):
    id: int
    status: str
    created_at: Optional[str] = None


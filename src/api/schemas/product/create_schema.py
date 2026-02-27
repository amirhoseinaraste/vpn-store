# import necessary packages
from pydantic import BaseModel
from typing import Optional

class CreateProduct(BaseModel):
    name: str
    category: int
    volume: int
    price: int
    duration: int
    status: Optional[str] = "available"
    

class responseCreateProductSchema(BaseModel):
    id: int
    status: str
    created_at: Optional[str] = None


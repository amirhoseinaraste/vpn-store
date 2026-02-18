# import necessary packages
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# get product by id schema
class ResponseGetOneProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None
    volume: int
    duration: int
    status : Optional[str] = None
    created_at: datetime
    updated_at : datetime


## import necessary packages
from pydantic import BaseModel
from typing import Optional


# get products schema
class ResponseGetAllProductsSchema(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    price: float
    volume: int
    duration: int
    status: str

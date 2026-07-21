# from necessary packages
from pydantic import BaseModel
from typing import Optional

class ResponseGetAllConfigsSchema(BaseModel):
    id: int
    product_id: int
    value: str

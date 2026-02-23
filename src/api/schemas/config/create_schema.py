# import from necessary packages
from pydantic import BaseModel
from typing import Optional

class CreateConfigSchema(BaseModel):
    product_id: str
    value: str

class ResponseCreateConfigSchema(BaseModel):
    id: int
    product_id: str
    value: str
    created_at: Optional[str] = None
    
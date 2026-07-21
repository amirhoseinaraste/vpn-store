# import from necessary packages
from pydantic import BaseModel
from typing import Optional

class CreateConfigSchema(BaseModel):
    product_id: int
    value: str

class ResponseCreateConfigSchema(BaseModel):
    id: int
    status: str
    created_at: Optional[str] = None
    
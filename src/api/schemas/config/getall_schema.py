# from necessary packages
from pydantic import BaseModel
from typing import Optional

class ResponseGetAllConfigsSchema(BaseModel):
    id: int
    product_id: str
    value: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    

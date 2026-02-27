# import from files

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

# create category schema
class CreateCategorySchema(BaseModel):
    name: str 
    tag: str
    description: Optional[str]
    parent_id: Optional[int] = None

class responseCreateCategorySchema(BaseModel):
    id: int
    status: str
    created_at: datetime
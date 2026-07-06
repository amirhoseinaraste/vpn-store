
# import from files

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

# create category schema
class UpdateCategorySchema(BaseModel):
    name: Optional[str]
    tag: Optional[str] 
    description: Optional[str]
    parent_id: Optional[int] 


class responseUpdateCategorySchema(BaseModel):
    name: str
    tag: str
    description: str
    parent_id: int
    created_at: str
    updated_at: str

# import from files
from pydantic import BaseModel, Field
from typing import Optional

# create category schema
class CreateCategorySchema(BaseModel):
    name: str = Field(..., example="VPN")
    tag: Optional[str] = Field(None, example="#vpn")
    description: Optional[str] = Field(None, example="A category for VPN products")
    parent_id: Optional[int] = Field(None, example=1)

class responseCreateCategorySchema(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    
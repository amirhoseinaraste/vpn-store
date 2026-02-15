# import necessary packages
from pydantic import BaseModel
from typing import Optional


# get user by id schema
class GetUserSchema(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: Optional[str] = None


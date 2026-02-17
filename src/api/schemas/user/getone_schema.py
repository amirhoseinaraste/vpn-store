# import necessary packages
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# get user by id schema
class GetUserSchema(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    status : Optional[str] = None
    created_at: datetime
    updated_at : datetime


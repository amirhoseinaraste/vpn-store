# import necessary packages
from pydantic import BaseModel
from typing import Optional

class CreateUserSchema(BaseModel):
    telegram_id: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class responseCreateUserSchema(BaseModel):
    id: int
    status: str
    created_at: Optional[str] = None


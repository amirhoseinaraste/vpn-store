## import necessary packages
from pydantic import BaseModel
from typing import Optional


# get users schema
class GetAllUsersSchema(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    
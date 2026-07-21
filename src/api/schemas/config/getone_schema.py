# from necessary packages
from pydantic import BaseModel
from typing import Optional

class ResponseGetOneConfigSchema(BaseModel):
    id: int
    value: str

## import necessary packages
from pydantic import BaseModel
from typing import Optional


# get products schema
class ResponseGetAllTransactionsSchema(BaseModel):
    id: int
    order_id: int
    photo_file_id: str
    archive_message_id: int
    status: str

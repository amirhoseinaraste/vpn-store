# import from files
from database import DB

# import from packages
from sqlalchemy import Column, Integer, String

# TODO: Init user model


class User(DB.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    telegram_id = Column(Integer, unique=True)
    username = Column(String, unique=True)
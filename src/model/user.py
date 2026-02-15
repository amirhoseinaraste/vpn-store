# import from files     
from src.DB.database import Base

# import from packages
from sqlalchemy import Column, Integer, String, BigInteger, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime
import uuid


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    status = Column(String, default='active')
    created_at = Column(Date)
    updated_at = Column(Date)
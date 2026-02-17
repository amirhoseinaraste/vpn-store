# import from files     
from src.DB.database import Base


# import from packages
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Enum
import datetime
import enum

class ProductStatus(enum.Enum):
    available = "available"
    inactive = "inactive"
    out_of_stock = "out_of_stock"


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Integer)
    volume = Column(Integer)
    duration = Column(Integer)
    status = Column(Enum(ProductStatus), default=ProductStatus.available)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime,  default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
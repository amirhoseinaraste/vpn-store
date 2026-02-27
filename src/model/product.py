# import from files     
from src.DB.database import Base


# import from packages
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, DateTime, Enum, Float
from sqlalchemy.orm import relationship
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
    price = Column(Float)
    volume = Column(Integer)
    duration = Column(Integer)
    # foreign key column matches existing database schema (category_id)
    category_id = Column(Integer, ForeignKey('categories.id'))
    status = Column(Enum(ProductStatus), default=ProductStatus.available)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # relationship to category object (singular)
    category_rel = relationship("Category", back_populates="products")









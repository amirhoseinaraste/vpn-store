# import from files
from src.DB.database import Base

# import from packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime


class Config(Base):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=True)
    value = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # product = relationship('Product', back_populates='configs')
    # transactions = relationship('Transaction', back_populates='config', cascade='all, delete-orphan')


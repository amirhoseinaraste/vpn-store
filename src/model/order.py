# from packages
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.orm import relationship
import datetime

# from files
from src.DB.database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.telegram_id"), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer)
    total_price = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    status = Column(String, default='pending')  # pending, completed, canceled

    user = relationship("User", backref="order")
    product = relationship("Product", backref="order")
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum, DECIMAL
from sqlalchemy.sql import func
from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(55))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    sku = Column(String(55), unique=True)
    price = Column(DECIMAL(10, 2))
    created_at = Column(DateTime, server_default=func.now())


class StockMovement(Base):
    __tablename__ = "stock_movements"

    stock_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity_change = Column(Integer)
    movement_type = Column(Enum("IN", "OUT"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, server_default=func.now())

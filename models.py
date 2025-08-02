# SQLAlchemy async model for Product
from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base

Base = declarative_base(cls=AsyncAttrs)

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (
        # Ensure SKU is unique and for faster lookups, index on name
        {'sqlite_autoincrement': True}
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, index=True)
    sku = Column(String(64), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Numeric(12, 2), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

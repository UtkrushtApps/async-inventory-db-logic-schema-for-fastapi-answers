from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from models import Product

# Async create product
def dict_to_product(data: dict) -> Product:
    return Product(**data)

async def create_product(db: AsyncSession, product_data: dict) -> Product:
    # product_data: dict with keys matching Product fields
    product = dict_to_product(product_data)
    db.add(product)
    try:
        await db.commit()
        await db.refresh(product)
    except IntegrityError:
        await db.rollback()
        raise
    return product

async def get_products(db: AsyncSession) -> List[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await db.execute(stmt)
    return result.scalars().all()

# Additional function for fetching by SKU (for uniqueness checks if needed)
async def get_product_by_sku(db: AsyncSession, sku: str) -> Optional[Product]:
    stmt = select(Product).where(Product.sku == sku)
    result = await db.execute(stmt)
    return result.scalars().first()

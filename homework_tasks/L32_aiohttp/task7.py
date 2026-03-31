"""
SQLAlchemy Async - Definicja Modelu: Zdefiniuj model Product używając
DeclarativeBase z SQLAlchemy . Model powinien mieć pola: id (int, klucz główny),
name (String(100)) oraz price (Integer, przechowujący cenę w groszach)
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Mapped, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

### MODELS ###
class Product(DeclarativeBase):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}


    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"
    
##### END TASK 7 REQUIREMENTS #####

### DATABASE ###

# Connect to the database
engine = create_async_engine("postgresql+asyncpg://postgres:asdf@localhost/aio_test_db")
session = AsyncSession(engine)

# Create the tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Product.metadata.create_all)


### HANDLERS ###

async def create_product(name, price):
    product = Product(name=name, price=price)
    session.add(product)
    await session.commit()
    return product

async def get_product(product_id=None, name=None):  # check if it shouldn't be saparated!
    if name is None and product_id is None:
        raise ValueError("Either product_id or name must be provided")

    # if name
    if name is not None:
        return await session.scalars(select(Product).where(Product.name == name))
    
    #if product_id
    return await session.get(Product, product_id)

async def get_all_products():
    return await session.scalars(select(Product))

    

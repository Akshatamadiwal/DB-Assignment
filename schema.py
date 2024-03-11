-- using ORM  SQLAlchemy in Python 

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, TIMESTAMP, DECIMAL, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product_Category(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    sku = Column(String(50))
    category_id = Column(Integer, ForeignKey('product_category.id'))
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'))
    price = Column(DECIMAL(10, 2))
    discount_id = Column(Integer, ForeignKey('discount.id'))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)
    category = relationship("Product_Category")
    inventory = relationship("Product_Inventory")
    discount = relationship("Discount")

class Product_Inventory(Base):
    __tablename__ = 'product_inventory'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)

class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    discount_percent = Column(DECIMAL(5, 2))
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)


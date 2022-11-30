from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker


Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100))
    selling_price = Column("selling_price", Float)
    buying_price = Column("buying_price",Float)

    def __init__(self, name, selling_price, buying_price):
        self.name = name
        self.selling_price = selling_price
        self.buying_price = buying_price





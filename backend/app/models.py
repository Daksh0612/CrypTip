from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, Float, ForeignKey
from sqlalchemy.sql import func
from ..database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user")  # admin / user

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True, nullable=False)
    chain = Column(String, nullable=False)  # ETH/BTC/etc
    category = Column(String, default="unknown")
    risk_score = Column(Float, default=0.0)
    tags = Column(String, default="")  # comma-separated simple tags
    metadata = Column(JSON, default={})
    date_added = Column(DateTime(timezone=True), server_default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, index=True)
    from_address = Column(String, nullable=False)
    to_address = Column(String, nullable=False)
    amount = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
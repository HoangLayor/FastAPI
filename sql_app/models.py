from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users" # Name of the table in the database

    id = Column(Integer, primary_key=True) # Primary key
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner") # Relationship with the Item table


class Item(Base):
    __tablename__ = "items" # Name of the table in the database

    id = Column(Integer, primary_key=True) # Primary key
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id")) # Foreign key

    owner = relationship("User", back_populates="items") # Relationship with the User table
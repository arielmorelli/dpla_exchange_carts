from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .cart import Cart

from . import Base

class Library(Base):
    __tablename__ = "library"

    lib_id = Column(String, primary_key=True)
    name = Column(String)
    credential = Column(String)

    carts = relationship(Cart)

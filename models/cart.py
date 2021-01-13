from sqlalchemy import Column, String, Boolean, ForeignKey

from . import Base

class Cart(Base):
    __tablename__ = "cart"

    name = Column(String, primary_key=True)
    library = Column(String, ForeignKey("library.lib_id"), nullable=False)
    endpoint = Column(String, nullable=True)
    cart_type = Column(String)
    is_enable = Column(Boolean, default=True)


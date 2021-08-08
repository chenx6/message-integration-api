from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from database import Base
from .zone import Zone


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    message = Column(String)
    img = Column(String)
    update_time = Column(DateTime)
    fetch_time = Column(DateTime)
    url = Column(String, unique=True)

    zone_id = Column(Integer, ForeignKey("zone.id"))
    zone = relationship("Zone", back_populates="items")

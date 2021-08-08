from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Zone(Base):
    __tablename__ = "zone"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    icon = Column(String)

    items = relationship("Item", back_populates="zone")

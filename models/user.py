from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base
from .user_zone import user_zone

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    subscribe_zones = relationship("Zone", secondary=user_zone)

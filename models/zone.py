from sqlalchemy import Column, Integer, String

from database import Base


class Zone(Base):
    __tablename__ = "zone"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(Integer)
    api_path = Column(String, unique=True)
    sub_url = Column(String)
    icon = Column(String)

from models.item import Item
from models.zone import Zone
from models.user import User
from database import engine, Base

Base.metadata.create_all(bind=engine)

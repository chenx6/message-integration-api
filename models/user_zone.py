from sqlalchemy import Table, Column, Integer, ForeignKey

from database import Base

user_zone = Table(
    "user_zone",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("zone_id", Integer, ForeignKey("zone.id")),
)

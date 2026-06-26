from sqlalchemy import Column, String, Text, ForeignKey
from database import Base

class ChampionPoints(Base):
    __tablename__ = "champion_points"

    build_id = Column(String, ForeignKey("builds.id"), primary_key=True)
    warfare = Column(Text)   # JSON string
    fitness = Column(Text)
    craft = Column(Text)

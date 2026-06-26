from sqlalchemy import Column, String, ForeignKey
from database import Base

class BuildGearItem(Base):
    __tablename__ = "build_gear_items"

    build_id = Column(String, ForeignKey("builds.id"), primary_key=True)
    gear_id = Column(String, ForeignKey("gear_items.id"), primary_key=True)


class CharacterBuild(Base):
    __tablename__ = "character_builds"

    character_id = Column(String, ForeignKey("characters.id"), primary_key=True)
    build_id = Column(String, ForeignKey("builds.id"), primary_key=True)

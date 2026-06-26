from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class GearSet(Base):
    __tablename__ = "gear_sets"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    # crafted, dungeon, trial, overland, pvp, monster, mythic
    set_type = Column(String)
    location = Column(String)
    num_pieces = Column(Integer)
    patch_version = Column(String)
    notes = Column(Text)
    last_updated = Column(String)

    bonuses = relationship("SetBonus", back_populates="gear_set", cascade="all, delete-orphan")
    gear_items = relationship("GearItem", back_populates="gear_set")


class SetBonus(Base):
    __tablename__ = "set_bonuses"

    id = Column(String, primary_key=True, index=True)
    set_id = Column(String, ForeignKey("gear_sets.id"), nullable=False)
    # 1–5: number of pieces needed to activate this bonus
    pieces_required = Column(Integer, nullable=False)
    bonus_description = Column(Text, nullable=False)
    # e.g. "Weapon Damage", "Max Health", "Critical Chance"
    stat_type = Column(String)
    stat_value = Column(Integer)

    gear_set = relationship("GearSet", back_populates="bonuses")

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class GearItem(Base):
    __tablename__ = "gear_items"

    id = Column(String, primary_key=True, index=True)
    set_name = Column(String, nullable=False)
    set_id = Column(String, ForeignKey("gear_sets.id"), nullable=True)
    slot = Column(String, nullable=False)
    weight = Column(String)
    trait = Column(String)
    quality = Column(String)
    obtained = Column(Integer)
    stickerbook_unlocked = Column(Integer)

    location = Column(String)
    source_notes = Column(Text)
    craftable = Column(Integer)
    transmute_cost = Column(Integer)

    notes = Column(Text)
    last_updated = Column(String)
    custom_icon = Column(String)

    gear_set = relationship("GearSet", back_populates="gear_items")
    enchantment = relationship("Enchantment", uselist=False, back_populates="gear")


class Enchantment(Base):
    __tablename__ = "gear_enchantments"

    gear_id = Column(String, ForeignKey("gear_items.id"), primary_key=True)
    type = Column(String)
    level = Column(String)
    quality = Column(String)
    obtained = Column(Integer)
    source = Column(String)

    gear = relationship("GearItem", back_populates="enchantment", foreign_keys=[gear_id])

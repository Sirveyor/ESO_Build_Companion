from sqlalchemy import Column, String, Text
from database import Base


class RefEnchantment(Base):
    __tablename__ = "ref_enchantments"
    id           = Column(String, primary_key=True)
    name         = Column(String, nullable=False)
    slot_type    = Column(String, nullable=False)  # Armor | Weapon | Jewelry
    effect       = Column(Text)
    essence_rune = Column(String)
    notes        = Column(Text)


class RefTrait(Base):
    __tablename__ = "ref_traits"
    id             = Column(String, primary_key=True)
    name           = Column(String, nullable=False)
    slot_type      = Column(String, nullable=False)  # Armor | Weapon | Jewelry
    effect         = Column(Text)
    trait_material = Column(String)
    notes          = Column(Text)


class RefMundusStone(Base):
    __tablename__ = "ref_mundus_stones"
    id        = Column(String, primary_key=True)
    name      = Column(String, nullable=False)
    effect    = Column(Text)
    stat_type = Column(String)
    location  = Column(Text)

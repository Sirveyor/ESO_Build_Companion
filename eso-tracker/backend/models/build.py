from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Build(Base):
    __tablename__ = "builds"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_name = Column("class", String, nullable=False)
    role = Column(String, nullable=False)
    patch_version = Column(String)
    source_link_id = Column(String, ForeignKey("source_links.id"))

    mundus_stone = Column(String)
    food_buff    = Column(String)
    attr_health  = Column(Integer)
    attr_magicka = Column(Integer)
    attr_stamina = Column(Integer)
    notes = Column(Text)
    last_updated = Column(String)
    favorite = Column(Integer)
    tags = Column(Text)

    gear_items = relationship("GearItem", secondary="build_gear_items")
    skills = relationship("Skill", secondary="build_skills")
    champion_points = relationship("ChampionPoints", uselist=False)

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from database import Base

class Trait(Base):
    __tablename__ = "traits"

    id = Column(String, primary_key=True, index=True)
    trait_type = Column(String, nullable=False)
    character_id = Column(String, ForeignKey("characters.id"), nullable=True)
    research_status = Column(String)
    research_end_time = Column(String)
    craftable = Column(Integer)
    notes = Column(Text)

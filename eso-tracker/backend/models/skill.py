from sqlalchemy import Column, String, Integer, Text
from database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    skill_line = Column(String, nullable=False)
    morph = Column(String)
    required_level = Column(Integer)
    obtained = Column(Integer)
    icon = Column(String)

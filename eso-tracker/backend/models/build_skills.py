from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base

class BuildSkill(Base):
    __tablename__ = "build_skills"

    build_id = Column(String, ForeignKey("builds.id"), primary_key=True)
    skill_id = Column(String, ForeignKey("skills.id"), primary_key=True)
    bar = Column(String, primary_key=True)
    position = Column(Integer, primary_key=True)
    is_ultimate = Column(Integer)

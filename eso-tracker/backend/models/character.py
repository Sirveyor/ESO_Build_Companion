from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_name = Column("class", String, nullable=False)
    race = Column(String, nullable=False)
    role = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    champion_points = Column(Integer, nullable=False)

    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    active_build_id = Column(String, ForeignKey("builds.id"))
    notes = Column(Text)
    last_updated = Column(String)
    custom_portrait = Column(String)

    user = relationship("User", back_populates="characters")
    builds = relationship("Build", secondary="character_builds")

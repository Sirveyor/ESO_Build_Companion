from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    display_name = Column(String)
    created_at = Column(String)

    characters = relationship("Character", back_populates="user")

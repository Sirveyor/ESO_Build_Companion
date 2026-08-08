from sqlalchemy import Column, String, ForeignKey
from database import Base


class LearnedFragment(Base):
    __tablename__ = "learned_fragments"

    id           = Column(String, primary_key=True)
    character_id = Column(String, ForeignKey("characters.id"), nullable=False)
    fragment_id  = Column(String, ForeignKey("ref_fragment_items.id"), nullable=False)
    learned_at   = Column(String)

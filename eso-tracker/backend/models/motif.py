from sqlalchemy import Column, String, ForeignKey
from database import Base


class LearnedMotif(Base):
    __tablename__ = "learned_motifs"

    id           = Column(String, primary_key=True)
    character_id = Column(String, ForeignKey("characters.id"), nullable=False)
    motif_id     = Column(String, ForeignKey("ref_motifs.id"), nullable=False)
    learned_at   = Column(String)

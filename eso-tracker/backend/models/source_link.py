from sqlalchemy import Column, String, Text
from database import Base


class SourceLink(Base):
    __tablename__ = "source_links"

    id = Column(String, primary_key=True, index=True)
    url = Column(String, nullable=False)
    site_name = Column(String)
    author = Column(String)
    patch_version = Column(String)
    last_checked = Column(String)
    notes = Column(Text)

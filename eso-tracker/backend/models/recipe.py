from sqlalchemy import Column, String, ForeignKey
from database import Base


class LearnedRecipe(Base):
    __tablename__ = "learned_recipes"

    id           = Column(String, primary_key=True)
    character_id = Column(String, ForeignKey("characters.id"), nullable=False)
    recipe_id    = Column(String, ForeignKey("ref_food.id"),   nullable=False)
    learned_at   = Column(String)

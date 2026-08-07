from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.recipe import LearnedRecipe
from schemas import LearnedRecipeSchema

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("/", response_model=list[LearnedRecipeSchema])
def get_learned_recipes(character_id: str = None, db: Session = Depends(get_db)):
    q = db.query(LearnedRecipe)
    if character_id:
        q = q.filter(LearnedRecipe.character_id == character_id)
    return q.all()


@router.post("/", response_model=LearnedRecipeSchema)
def learn_recipe(data: LearnedRecipeSchema, db: Session = Depends(get_db)):
    row = LearnedRecipe(**data.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{recipe_id}")
def unlearn_recipe(recipe_id: str, db: Session = Depends(get_db)):
    row = db.query(LearnedRecipe).filter(LearnedRecipe.id == recipe_id).first()
    if row:
        db.delete(row)
        db.commit()
    return {"detail": "deleted"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.fragment import LearnedFragment
from schemas import LearnedFragmentSchema

router = APIRouter(prefix="/fragments", tags=["Fragments"])


@router.get("/", response_model=list[LearnedFragmentSchema])
def get_learned_fragments(character_id: str = None, db: Session = Depends(get_db)):
    q = db.query(LearnedFragment)
    if character_id:
        q = q.filter(LearnedFragment.character_id == character_id)
    return q.all()


@router.post("/", response_model=LearnedFragmentSchema)
def learn_fragment(data: LearnedFragmentSchema, db: Session = Depends(get_db)):
    row = LearnedFragment(**data.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{fragment_id}")
def unlearn_fragment(fragment_id: str, db: Session = Depends(get_db)):
    row = db.query(LearnedFragment).filter(LearnedFragment.id == fragment_id).first()
    if row:
        db.delete(row)
        db.commit()
    return {"detail": "deleted"}

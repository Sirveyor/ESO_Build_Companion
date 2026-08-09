from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.motif import LearnedMotif
from schemas import LearnedMotifSchema

router = APIRouter(prefix="/motifs", tags=["Motifs"])


@router.get("/", response_model=list[LearnedMotifSchema])
def get_learned_motifs(character_id: str = None, db: Session = Depends(get_db)):
    q = db.query(LearnedMotif)
    if character_id:
        q = q.filter(LearnedMotif.character_id == character_id)
    return q.all()


@router.post("/", response_model=LearnedMotifSchema)
def learn_motif(data: LearnedMotifSchema, db: Session = Depends(get_db)):
    row = LearnedMotif(**data.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.delete("/{motif_id}")
def unlearn_motif(motif_id: str, db: Session = Depends(get_db)):
    row = db.query(LearnedMotif).filter(LearnedMotif.id == motif_id).first()
    if row:
        db.delete(row)
        db.commit()
    return {"detail": "deleted"}

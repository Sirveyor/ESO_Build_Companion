from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.trait import Trait
from schemas import TraitSchema


router = APIRouter(prefix="/traits", tags=["Traits"])


@router.get("/", response_model=list[TraitSchema])
def get_traits(db: Session = Depends(get_db)):
    return db.query(Trait).all()


@router.post("/", response_model=TraitSchema)
def create_trait(trait: TraitSchema, db: Session = Depends(get_db)):
    db_trait = Trait(**trait.model_dump())
    db.add(db_trait)
    db.commit()
    db.refresh(db_trait)
    return db_trait


@router.get("/{trait_id}", response_model=TraitSchema)
def get_trait(trait_id: str, db: Session = Depends(get_db)):
    trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if not trait:
        raise HTTPException(status_code=404, detail="Trait not found")
    return trait


@router.put("/{trait_id}", response_model=TraitSchema)
def update_trait(trait_id: str, updated: TraitSchema, db: Session = Depends(get_db)):
    trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if not trait:
        raise HTTPException(status_code=404, detail="Trait not found")
    for key, value in updated.model_dump().items():
        setattr(trait, key, value)
    db.commit()
    db.refresh(trait)
    return trait


@router.delete("/{trait_id}")
def delete_trait(trait_id: str, db: Session = Depends(get_db)):
    trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if not trait:
        raise HTTPException(status_code=404, detail="Trait not found")
    db.delete(trait)
    db.commit()
    return {"detail": "Trait deleted"}


@router.put("/{trait_id}/research")
def start_research(trait_id: str, research_end_time: str, db: Session = Depends(get_db)):
    trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if not trait:
        raise HTTPException(status_code=404, detail="Trait not found")
    trait.research_status = "in_progress"
    trait.research_end_time = research_end_time
    db.commit()
    return {"trait_id": trait_id, "research_status": trait.research_status,
            "research_end_time": trait.research_end_time}


@router.put("/{trait_id}/complete")
def complete_research(trait_id: str, db: Session = Depends(get_db)):
    trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if not trait:
        raise HTTPException(status_code=404, detail="Trait not found")
    trait.research_status = "complete"
    trait.research_end_time = None
    db.commit()
    return {"trait_id": trait_id, "research_status": trait.research_status}

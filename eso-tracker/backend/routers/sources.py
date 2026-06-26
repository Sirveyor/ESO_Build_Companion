from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.source_link import SourceLink
from schemas import SourceLinkSchema


router = APIRouter(prefix="/sources", tags=["Sources"])


@router.get("/", response_model=list[SourceLinkSchema])
def get_sources(db: Session = Depends(get_db)):
    return db.query(SourceLink).all()


@router.post("/", response_model=SourceLinkSchema)
def create_source(source: SourceLinkSchema, db: Session = Depends(get_db)):
    db_source = SourceLink(**source.model_dump())
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source


@router.get("/{source_id}", response_model=SourceLinkSchema)
def get_source(source_id: str, db: Session = Depends(get_db)):
    source = db.query(SourceLink).filter(SourceLink.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source


@router.put("/{source_id}", response_model=SourceLinkSchema)
def update_source(source_id: str, updated: SourceLinkSchema, db: Session = Depends(get_db)):
    source = db.query(SourceLink).filter(SourceLink.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    for key, value in updated.model_dump().items():
        setattr(source, key, value)
    db.commit()
    db.refresh(source)
    return source


@router.delete("/{source_id}")
def delete_source(source_id: str, db: Session = Depends(get_db)):
    source = db.query(SourceLink).filter(SourceLink.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    db.delete(source)
    db.commit()
    return {"detail": "Source deleted"}

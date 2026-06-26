from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.build import Build
from models.gear_item import GearItem
from models.links import BuildGearItem
from schemas import BuildSchema, GearItemSchema


router = APIRouter(prefix="/builds", tags=["Builds"])


@router.get("/", response_model=list[BuildSchema])
def get_builds(db: Session = Depends(get_db)):
    return db.query(Build).all()


@router.post("/", response_model=BuildSchema)
def create_build(build: BuildSchema, db: Session = Depends(get_db)):
    db_build = Build(**build.model_dump())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build


@router.get("/{build_id}", response_model=BuildSchema)
def get_build(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    return build


@router.put("/{build_id}", response_model=BuildSchema)
def update_build(build_id: str, updated: BuildSchema, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    for key, value in updated.model_dump().items():
        setattr(build, key, value)
    db.commit()
    db.refresh(build)
    return build


@router.delete("/{build_id}")
def delete_build(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    db.delete(build)
    db.commit()
    return {"detail": "Build deleted"}


@router.get("/{build_id}/gear", response_model=list[GearItemSchema])
def get_build_gear(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    return build.gear_items


@router.post("/{build_id}/gear", response_model=GearItemSchema)
def add_gear_to_build(build_id: str, gear: GearItemSchema, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    db_gear = GearItem(**gear.model_dump(exclude={"enchantment"}))
    db.add(db_gear)
    db.flush()
    db.add(BuildGearItem(build_id=build_id, gear_id=db_gear.id))
    db.commit()
    db.refresh(db_gear)
    return db_gear


@router.get("/{build_id}/completion")
def get_completion(build_id: str, db: Session = Depends(get_db)):
    build = db.query(Build).filter(Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    total = len(build.gear_items)
    obtained = sum(1 for g in build.gear_items if g.obtained)
    return {"build_id": build_id, "total_pieces": total, "obtained": obtained,
            "percent": round(obtained / total * 100) if total else 0}


@router.post("/{build_id}/duplicate")
def duplicate_build(build_id: str):
    return {"message": "Duplicate build — not yet implemented", "id": build_id}

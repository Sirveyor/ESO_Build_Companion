from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.gear_set import GearSet, SetBonus
from schemas import GearSetSchema, SetBonusSchema


router = APIRouter(prefix="/gear-sets", tags=["Gear Sets"])


@router.get("/", response_model=list[GearSetSchema])
def get_gear_sets(db: Session = Depends(get_db)):
    return db.query(GearSet).all()


@router.post("/", response_model=GearSetSchema)
def create_gear_set(gear_set: GearSetSchema, db: Session = Depends(get_db)):
    existing = db.query(GearSet).filter(GearSet.name == gear_set.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="A gear set with that name already exists")
    db_set = GearSet(**gear_set.model_dump(exclude={"bonuses"}))
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set


@router.get("/compare", response_model=list[GearSetSchema])
def compare_gear_sets(set_ids: str, db: Session = Depends(get_db)):
    """Pass comma-separated set IDs: /gear-sets/compare?set_ids=id1,id2"""
    ids = [s.strip() for s in set_ids.split(",") if s.strip()]
    if len(ids) < 2:
        raise HTTPException(status_code=400, detail="Provide at least two set IDs to compare")
    sets = db.query(GearSet).filter(GearSet.id.in_(ids)).all()
    if len(sets) != len(ids):
        raise HTTPException(status_code=404, detail="One or more gear sets not found")
    return sets


@router.get("/{set_id}", response_model=GearSetSchema)
def get_gear_set(set_id: str, db: Session = Depends(get_db)):
    gear_set = db.query(GearSet).filter(GearSet.id == set_id).first()
    if not gear_set:
        raise HTTPException(status_code=404, detail="Gear set not found")
    return gear_set


@router.put("/{set_id}", response_model=GearSetSchema)
def update_gear_set(set_id: str, updated: GearSetSchema, db: Session = Depends(get_db)):
    gear_set = db.query(GearSet).filter(GearSet.id == set_id).first()
    if not gear_set:
        raise HTTPException(status_code=404, detail="Gear set not found")
    for key, value in updated.model_dump(exclude={"bonuses"}).items():
        setattr(gear_set, key, value)
    db.commit()
    db.refresh(gear_set)
    return gear_set


@router.delete("/{set_id}")
def delete_gear_set(set_id: str, db: Session = Depends(get_db)):
    gear_set = db.query(GearSet).filter(GearSet.id == set_id).first()
    if not gear_set:
        raise HTTPException(status_code=404, detail="Gear set not found")
    db.delete(gear_set)
    db.commit()
    return {"detail": "Gear set deleted"}


@router.get("/{set_id}/bonuses", response_model=list[SetBonusSchema])
def get_set_bonuses(set_id: str, db: Session = Depends(get_db)):
    gear_set = db.query(GearSet).filter(GearSet.id == set_id).first()
    if not gear_set:
        raise HTTPException(status_code=404, detail="Gear set not found")
    return gear_set.bonuses


@router.post("/{set_id}/bonuses", response_model=SetBonusSchema)
def add_set_bonus(set_id: str, bonus: SetBonusSchema, db: Session = Depends(get_db)):
    gear_set = db.query(GearSet).filter(GearSet.id == set_id).first()
    if not gear_set:
        raise HTTPException(status_code=404, detail="Gear set not found")
    db_bonus = SetBonus(**{**bonus.model_dump(), "set_id": set_id})
    db.add(db_bonus)
    db.commit()
    db.refresh(db_bonus)
    return db_bonus


@router.put("/{set_id}/bonuses/{bonus_id}", response_model=SetBonusSchema)
def update_set_bonus(set_id: str, bonus_id: str, updated: SetBonusSchema,
                     db: Session = Depends(get_db)):
    bonus = db.query(SetBonus).filter(
        SetBonus.id == bonus_id, SetBonus.set_id == set_id
    ).first()
    if not bonus:
        raise HTTPException(status_code=404, detail="Set bonus not found")
    for key, value in updated.model_dump().items():
        setattr(bonus, key, value)
    db.commit()
    db.refresh(bonus)
    return bonus


@router.delete("/{set_id}/bonuses/{bonus_id}")
def delete_set_bonus(set_id: str, bonus_id: str, db: Session = Depends(get_db)):
    bonus = db.query(SetBonus).filter(
        SetBonus.id == bonus_id, SetBonus.set_id == set_id
    ).first()
    if not bonus:
        raise HTTPException(status_code=404, detail="Set bonus not found")
    db.delete(bonus)
    db.commit()
    return {"detail": "Set bonus deleted"}

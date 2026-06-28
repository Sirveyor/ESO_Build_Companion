from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.gear_item import Enchantment, GearItem
from models.links import BuildGearItem
from schemas import GearItemSchema, EnchantmentSchema


router = APIRouter(prefix="/gear", tags=["Gear"])


@router.get("/", response_model=list[GearItemSchema])
def get_gear(db: Session = Depends(get_db)):
    return db.query(GearItem).all()


@router.post("/", response_model=GearItemSchema)
def create_gear(gear: GearItemSchema, db: Session = Depends(get_db)):
    data = gear.model_dump(exclude={"enchantment"})
    db_gear = GearItem(**data)
    db.add(db_gear)
    db.commit()
    db.refresh(db_gear)
    return db_gear


@router.get("/{gear_id}", response_model=GearItemSchema)
def get_gear_item(gear_id: str, db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    return item


@router.put("/{gear_id}", response_model=GearItemSchema)
def update_gear(gear_id: str, updated: GearItemSchema, db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    for key, value in updated.model_dump(exclude={"enchantment"}).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{gear_id}")
def delete_gear(gear_id: str, db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    db.query(BuildGearItem).filter(BuildGearItem.gear_id == gear_id).delete()
    db.delete(item)
    db.commit()
    return {"detail": "Gear item deleted"}


@router.put("/{gear_id}/obtained")
def toggle_gear_obtained(gear_id: str, db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    item.obtained = 0 if item.obtained else 1
    db.commit()
    return {"obtained": item.obtained}


@router.put("/{gear_id}/stickerbook")
def toggle_gear_stickerbook(gear_id: str, db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    item.stickerbook_unlocked = 0 if item.stickerbook_unlocked else 1
    db.commit()
    return {"stickerbook_unlocked": item.stickerbook_unlocked}


@router.put("/{gear_id}/enchantment", response_model=EnchantmentSchema)
def update_enchantment(gear_id: str, enchantment_data: EnchantmentSchema,
                       db: Session = Depends(get_db)):
    item = db.query(GearItem).filter(GearItem.id == gear_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Gear item not found")
    existing = db.query(Enchantment).filter(Enchantment.gear_id == gear_id).first()
    if existing:
        for key, value in enchantment_data.model_dump().items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    new_enc = Enchantment(**enchantment_data.model_dump())
    db.add(new_enc)
    db.commit()
    db.refresh(new_enc)
    return new_enc

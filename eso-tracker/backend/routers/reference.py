from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reference import RefEnchantment, RefTrait, RefMundusStone
from schemas import RefEnchantmentSchema, RefTraitSchema, RefMundusStoneSchema

router = APIRouter(prefix="/reference", tags=["Reference"])


@router.get("/enchantments", response_model=list[RefEnchantmentSchema])
def get_ref_enchantments(slot_type: str = None, db: Session = Depends(get_db)):
    q = db.query(RefEnchantment)
    if slot_type:
        q = q.filter(RefEnchantment.slot_type == slot_type)
    return q.order_by(RefEnchantment.slot_type, RefEnchantment.name).all()


@router.get("/traits", response_model=list[RefTraitSchema])
def get_ref_traits(slot_type: str = None, db: Session = Depends(get_db)):
    q = db.query(RefTrait)
    if slot_type:
        q = q.filter(RefTrait.slot_type == slot_type)
    return q.order_by(RefTrait.slot_type, RefTrait.name).all()


@router.get("/mundus-stones", response_model=list[RefMundusStoneSchema])
def get_ref_mundus_stones(db: Session = Depends(get_db)):
    return db.query(RefMundusStone).order_by(RefMundusStone.name).all()

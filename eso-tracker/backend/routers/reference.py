from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reference import RefEnchantment, RefTrait, RefMundusStone, RefSkillLine, RefSkill, RefResearchTrait, RefFood, RefWeaponType, RefMotif, RefFragmentSet
from schemas import RefEnchantmentSchema, RefTraitSchema, RefMundusStoneSchema, RefSkillLineSchema, RefSkillSchema, RefResearchTraitSchema, RefFoodSchema, RefWeaponTypeSchema, RefMotifSchema, RefFragmentSetSchema

router = APIRouter(prefix="/reference", tags=["Reference"])


@router.get("/enchantments", response_model=list[RefEnchantmentSchema])
def get_ref_enchantments(slot_type: str = None, db: Session = Depends(get_db)):
    q = db.query(RefEnchantment)
    if slot_type:
        q = q.filter(RefEnchantment.slot_type == slot_type)
    return q.order_by(RefEnchantment.slot_type, RefEnchantment.name).all()


@router.post("/enchantments", response_model=RefEnchantmentSchema)
def create_ref_enchantment(item: RefEnchantmentSchema, db: Session = Depends(get_db)):
    db_item = RefEnchantment(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.put("/enchantments/{item_id}", response_model=RefEnchantmentSchema)
def update_ref_enchantment(item_id: str, updated: RefEnchantmentSchema, db: Session = Depends(get_db)):
    item = db.query(RefEnchantment).filter(RefEnchantment.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Enchantment not found")
    for key, value in updated.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/enchantments/{item_id}")
def delete_ref_enchantment(item_id: str, db: Session = Depends(get_db)):
    item = db.query(RefEnchantment).filter(RefEnchantment.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Enchantment not found")
    db.delete(item)
    db.commit()
    return {"detail": "Enchantment deleted"}


@router.get("/traits", response_model=list[RefTraitSchema])
def get_ref_traits(slot_type: str = None, db: Session = Depends(get_db)):
    q = db.query(RefTrait)
    if slot_type:
        q = q.filter(RefTrait.slot_type == slot_type)
    return q.order_by(RefTrait.slot_type, RefTrait.name).all()


@router.post("/traits", response_model=RefTraitSchema)
def create_ref_trait(item: RefTraitSchema, db: Session = Depends(get_db)):
    db_item = RefTrait(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.put("/traits/{item_id}", response_model=RefTraitSchema)
def update_ref_trait(item_id: str, updated: RefTraitSchema, db: Session = Depends(get_db)):
    item = db.query(RefTrait).filter(RefTrait.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Trait not found")
    for key, value in updated.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/traits/{item_id}")
def delete_ref_trait(item_id: str, db: Session = Depends(get_db)):
    item = db.query(RefTrait).filter(RefTrait.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Trait not found")
    db.delete(item)
    db.commit()
    return {"detail": "Trait deleted"}


@router.get("/mundus-stones", response_model=list[RefMundusStoneSchema])
def get_ref_mundus_stones(db: Session = Depends(get_db)):
    return db.query(RefMundusStone).order_by(RefMundusStone.name).all()


@router.post("/mundus-stones", response_model=RefMundusStoneSchema)
def create_ref_mundus_stone(item: RefMundusStoneSchema, db: Session = Depends(get_db)):
    db_item = RefMundusStone(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.put("/mundus-stones/{item_id}", response_model=RefMundusStoneSchema)
def update_ref_mundus_stone(item_id: str, updated: RefMundusStoneSchema, db: Session = Depends(get_db)):
    item = db.query(RefMundusStone).filter(RefMundusStone.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Mundus stone not found")
    for key, value in updated.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/mundus-stones/{item_id}")
def delete_ref_mundus_stone(item_id: str, db: Session = Depends(get_db)):
    item = db.query(RefMundusStone).filter(RefMundusStone.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Mundus stone not found")
    db.delete(item)
    db.commit()
    return {"detail": "Mundus stone deleted"}


@router.get("/skill-lines", response_model=list[RefSkillLineSchema])
def get_ref_skill_lines(category: str = None, class_name: str = None, db: Session = Depends(get_db)):
    q = db.query(RefSkillLine)
    if category:
        q = q.filter(RefSkillLine.category == category)
    if class_name:
        q = q.filter(
            (RefSkillLine.class_name == class_name) | (RefSkillLine.class_name == None)  # noqa: E711
        )
    return q.order_by(RefSkillLine.category, RefSkillLine.name).all()


@router.get("/skills", response_model=list[RefSkillSchema])
def get_ref_skills(skill_line_id: str = None, db: Session = Depends(get_db)):
    q = db.query(RefSkill)
    if skill_line_id:
        q = q.filter(RefSkill.skill_line_id == skill_line_id)
    return q.order_by(RefSkill.is_ultimate, RefSkill.name).all()


@router.get("/research-traits", response_model=list[RefResearchTraitSchema])
def get_ref_research_traits(slot_category: str = None, db: Session = Depends(get_db)):
    q = db.query(RefResearchTrait)
    if slot_category:
        q = q.filter(RefResearchTrait.slot_category == slot_category)
    return q.order_by(RefResearchTrait.slot_category, RefResearchTrait.item_type, RefResearchTrait.trait_name).all()


@router.get("/food", response_model=list[RefFoodSchema])
def get_ref_food(food_type: str = None, db: Session = Depends(get_db)):
    q = db.query(RefFood)
    if food_type:
        q = q.filter(RefFood.food_type == food_type)
    return q.order_by(RefFood.food_type, RefFood.name).all()


@router.get("/weapon-types", response_model=list[RefWeaponTypeSchema])
def get_ref_weapon_types(db: Session = Depends(get_db)):
    return db.query(RefWeaponType).order_by(RefWeaponType.sort_order).all()


@router.get("/motifs", response_model=list[RefMotifSchema])
def get_ref_motifs(category: str = None, db: Session = Depends(get_db)):
    q = db.query(RefMotif)
    if category:
        q = q.filter(RefMotif.category == category)
    return q.order_by(RefMotif.category, RefMotif.motif_number, RefMotif.name).all()


@router.get("/fragments", response_model=list[RefFragmentSetSchema])
def get_ref_fragments(category: str = None, db: Session = Depends(get_db)):
    q = db.query(RefFragmentSet)
    if category:
        q = q.filter(RefFragmentSet.category == category)
    return q.order_by(RefFragmentSet.category, RefFragmentSet.name).all()

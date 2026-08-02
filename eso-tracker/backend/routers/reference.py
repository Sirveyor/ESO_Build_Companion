from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reference import RefEnchantment, RefTrait, RefMundusStone, RefSkillLine, RefSkill, RefResearchTrait, RefFood, RefWeaponType
from schemas import RefEnchantmentSchema, RefTraitSchema, RefMundusStoneSchema, RefSkillLineSchema, RefSkillSchema, RefResearchTraitSchema, RefFoodSchema, RefWeaponTypeSchema

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

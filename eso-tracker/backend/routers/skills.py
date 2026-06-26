from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.skill import Skill
from schemas import SkillSchema


router = APIRouter(prefix="/skills", tags=["Skills"])


@router.get("/", response_model=list[SkillSchema])
def get_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()


@router.post("/", response_model=SkillSchema)
def create_skill(skill: SkillSchema, db: Session = Depends(get_db)):
    db_skill = Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


@router.get("/{skill_id}", response_model=SkillSchema)
def get_skill(skill_id: str, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.put("/{skill_id}", response_model=SkillSchema)
def update_skill(skill_id: str, updated: SkillSchema, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    for key, value in updated.model_dump().items():
        setattr(skill, key, value)
    db.commit()
    db.refresh(skill)
    return skill


@router.delete("/{skill_id}")
def delete_skill(skill_id: str, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"detail": "Skill deleted"}


@router.put("/{skill_id}/obtained")
def toggle_skill_obtained(skill_id: str, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    skill.obtained = 0 if skill.obtained else 1
    db.commit()
    return {"obtained": skill.obtained}

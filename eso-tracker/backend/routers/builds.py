import uuid
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models.build import Build
from models.build_skills import BuildSkill
from models.champion_points import ChampionPoints
from models.gear_item import GearItem
from models.links import BuildGearItem, CharacterBuild
from models.skill import Skill
from schemas import BuildSchema, GearItemSchema, SkillSchema, BuildSkillAssignmentSchema, ChampionPointsSchema

router = APIRouter(prefix="/builds", tags=["Builds"])


# ── Build CRUD ────────────────────────────────────────────────────────────────

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


# ── Gear ──────────────────────────────────────────────────────────────────────

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


# ── Duplicate ─────────────────────────────────────────────────────────────────

@router.post("/{build_id}/duplicate", response_model=BuildSchema)
def duplicate_build(build_id: str, db: Session = Depends(get_db)):
    original = db.query(Build).filter(Build.id == build_id).first()
    if not original:
        raise HTTPException(status_code=404, detail="Build not found")

    new_id = str(uuid.uuid4())
    new_build = Build(
        id=new_id,
        name=f"{original.name} (Copy)",
        class_name=original.class_name,
        role=original.role,
        mundus_stone=original.mundus_stone,
        food_buff=original.food_buff,
        attr_health=original.attr_health,
        attr_magicka=original.attr_magicka,
        attr_stamina=original.attr_stamina,
        patch_version=original.patch_version,
        source_link_id=original.source_link_id,
        notes=original.notes,
        last_updated=datetime.now(timezone.utc).isoformat(),
        favorite=0,
        tags=original.tags,
    )
    db.add(new_build)
    db.flush()

    # Deep-copy gear items (reset obtained status)
    for gear in original.gear_items:
        new_gear_id = str(uuid.uuid4())
        db.add(GearItem(
            id=new_gear_id,
            set_name=gear.set_name,
            set_id=gear.set_id,
            slot=gear.slot,
            weight=gear.weight,
            trait=gear.trait,
            quality=gear.quality,
            obtained=0,
            stickerbook_unlocked=gear.stickerbook_unlocked,
            location=gear.location,
            source_notes=gear.source_notes,
            craftable=gear.craftable,
            transmute_cost=gear.transmute_cost,
            notes=gear.notes,
            last_updated=datetime.now(timezone.utc).isoformat(),
            custom_icon=gear.custom_icon,
        ))
        db.flush()
        db.add(BuildGearItem(build_id=new_id, gear_id=new_gear_id))

    # Link to the same character(s) as the original
    for link in db.query(CharacterBuild).filter(CharacterBuild.build_id == build_id).all():
        db.add(CharacterBuild(character_id=link.character_id, build_id=new_id))

    db.commit()
    db.refresh(new_build)
    return new_build


# ── Skills ────────────────────────────────────────────────────────────────────

@router.get("/{build_id}/skills", response_model=list[BuildSkillAssignmentSchema])
def get_build_skills(build_id: str, db: Session = Depends(get_db)):
    if not db.query(Build).filter(Build.id == build_id).first():
        raise HTTPException(status_code=404, detail="Build not found")
    assignments = db.query(BuildSkill).filter(BuildSkill.build_id == build_id).all()
    result = []
    for a in assignments:
        skill = db.query(Skill).filter(Skill.id == a.skill_id).first()
        if skill:
            result.append(BuildSkillAssignmentSchema(
                skill=SkillSchema.model_validate(skill),
                bar=a.bar,
                position=a.position,
                is_ultimate=a.is_ultimate,
            ))
    return result


@router.post("/{build_id}/skills", response_model=BuildSkillAssignmentSchema)
def set_build_skill(build_id: str, payload: dict, db: Session = Depends(get_db)):
    """Assign a skill to a bar/position slot. Overwrites any existing assignment at that slot.
    Payload: {skill: {name, skill_line, morph?, obtained?}, bar, position, is_ultimate}
    """
    if not db.query(Build).filter(Build.id == build_id).first():
        raise HTTPException(status_code=404, detail="Build not found")

    skill_data = payload.get("skill", {})
    bar        = payload.get("bar", "bar1")
    position   = int(payload.get("position", 0))
    is_ult     = int(payload.get("is_ultimate", 0))

    # Find or create the skill (match by name + skill_line to avoid duplicates)
    skill = db.query(Skill).filter(
        Skill.name == skill_data.get("name", ""),
        Skill.skill_line == skill_data.get("skill_line", ""),
    ).first()
    if not skill:
        skill = Skill(
            id=str(uuid.uuid4()),
            name=skill_data.get("name", ""),
            skill_line=skill_data.get("skill_line", ""),
            morph=skill_data.get("morph"),
            required_level=skill_data.get("required_level"),
            obtained=int(skill_data.get("obtained", 0)),
        )
        db.add(skill)
        db.flush()

    # Replace any existing assignment at this bar/position
    existing = db.query(BuildSkill).filter(
        BuildSkill.build_id == build_id,
        BuildSkill.bar == bar,
        BuildSkill.position == position,
    ).first()
    if existing:
        db.delete(existing)
        db.flush()

    db.add(BuildSkill(build_id=build_id, skill_id=skill.id,
                      bar=bar, position=position, is_ultimate=is_ult))
    db.commit()
    db.refresh(skill)
    return BuildSkillAssignmentSchema(
        skill=SkillSchema.model_validate(skill),
        bar=bar, position=position, is_ultimate=is_ult,
    )


@router.delete("/{build_id}/skills/{bar}/{position}")
def clear_skill_slot(build_id: str, bar: str, position: int, db: Session = Depends(get_db)):
    """Clear the skill at a specific bar/position slot."""
    assignment = db.query(BuildSkill).filter(
        BuildSkill.build_id == build_id,
        BuildSkill.bar == bar,
        BuildSkill.position == position,
    ).first()
    if assignment:
        db.delete(assignment)
        db.commit()
    return {"detail": "Slot cleared"}


# ── Champion Points ───────────────────────────────────────────────────────────

@router.get("/{build_id}/champion-points", response_model=ChampionPointsSchema)
def get_champion_points(build_id: str, db: Session = Depends(get_db)):
    if not db.query(Build).filter(Build.id == build_id).first():
        raise HTTPException(status_code=404, detail="Build not found")
    cp = db.query(ChampionPoints).filter(ChampionPoints.build_id == build_id).first()
    if not cp:
        return ChampionPointsSchema(build_id=build_id)
    return cp


@router.put("/{build_id}/champion-points", response_model=ChampionPointsSchema)
def save_champion_points(build_id: str, body: ChampionPointsSchema, db: Session = Depends(get_db)):
    if not db.query(Build).filter(Build.id == build_id).first():
        raise HTTPException(status_code=404, detail="Build not found")
    cp = db.query(ChampionPoints).filter(ChampionPoints.build_id == build_id).first()
    if not cp:
        cp = ChampionPoints(build_id=build_id)
        db.add(cp)
    cp.warfare = body.warfare
    cp.fitness = body.fitness
    cp.craft   = body.craft
    db.commit()
    db.refresh(cp)
    return cp

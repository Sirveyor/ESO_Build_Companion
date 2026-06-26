from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from dependencies import get_db
from models.character import Character
from models.build import Build
from models.links import CharacterBuild
from schemas import CharacterSchema, BuildSchema


router = APIRouter(prefix="/characters", tags=["Characters"])


@router.get("/", response_model=list[CharacterSchema])
def get_characters(user_id: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Character)
    if user_id:
        query = query.filter(Character.user_id == user_id)
    return query.all()


@router.post("/", response_model=CharacterSchema)
def create_character(character: CharacterSchema, db: Session = Depends(get_db)):
    db_char = Character(**character.model_dump())
    db.add(db_char)
    db.commit()
    db.refresh(db_char)
    return db_char


@router.get("/{character_id}", response_model=CharacterSchema)
def get_character(character_id: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@router.put("/{character_id}", response_model=CharacterSchema)
def update_character(character_id: str, updated: CharacterSchema, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in updated.model_dump().items():
        setattr(character, key, value)
    db.commit()
    db.refresh(character)
    return character


@router.delete("/{character_id}")
def delete_character(character_id: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(character)
    db.commit()
    return {"detail": "Character deleted"}


@router.get("/{character_id}/builds", response_model=list[BuildSchema])
def get_character_builds(character_id: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character.builds


@router.post("/{character_id}/builds", response_model=BuildSchema)
def create_build_for_character(character_id: str, build: BuildSchema,
                                db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db_build = Build(**build.model_dump())
    db.add(db_build)
    db.flush()
    db.add(CharacterBuild(character_id=character_id, build_id=db_build.id))
    db.commit()
    db.refresh(db_build)
    return db_build


@router.put("/{character_id}/active_build")
def set_active_build(character_id: str, build_id: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    character.active_build_id = build_id
    db.commit()
    return {"character_id": character_id, "active_build_id": build_id}

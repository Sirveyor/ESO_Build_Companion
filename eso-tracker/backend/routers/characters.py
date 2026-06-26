from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.character import Character
from schemas import CharacterSchema


router = APIRouter(prefix="/characters", tags=["Characters"])


@router.get("/", response_model=list[CharacterSchema])
def get_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()


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


@router.put("/{character_id}/active_build")
def set_active_build(character_id: str, build_id: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    character.active_build_id = build_id
    db.commit()
    return {"character_id": character_id, "active_build_id": build_id}

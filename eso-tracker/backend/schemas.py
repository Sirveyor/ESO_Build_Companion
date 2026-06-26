from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserSchema(BaseModel):
    id: str
    name: str
    display_name: Optional[str] = None
    created_at: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class CharacterSchema(BaseModel):
    id: str
    name: str
    class_name: str
    race: str
    role: str
    level: int
    champion_points: int
    user_id: Optional[str] = None
    active_build_id: Optional[str] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None
    custom_portrait: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class BuildSchema(BaseModel):
    id: str
    name: str
    class_name: str
    role: str
    patch_version: Optional[str] = None
    source_link_id: Optional[str] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None
    favorite: Optional[int] = None
    tags: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class SetBonusSchema(BaseModel):
    id: str
    set_id: str
    pieces_required: int
    bonus_description: str
    stat_type: Optional[str] = None
    stat_value: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class GearSetSchema(BaseModel):
    id: str
    name: str
    set_type: Optional[str] = None
    location: Optional[str] = None
    num_pieces: Optional[int] = None
    patch_version: Optional[str] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None
    bonuses: list[SetBonusSchema] = []

    model_config = ConfigDict(from_attributes=True)


class EnchantmentSchema(BaseModel):
    gear_id: str
    type: Optional[str] = None
    level: Optional[str] = None
    quality: Optional[str] = None
    obtained: Optional[int] = None
    source: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class GearItemSchema(BaseModel):
    id: str
    set_name: str
    set_id: Optional[str] = None
    slot: str
    weight: Optional[str] = None
    trait: Optional[str] = None
    quality: Optional[str] = None
    obtained: Optional[int] = None
    stickerbook_unlocked: Optional[int] = None
    location: Optional[str] = None
    source_notes: Optional[str] = None
    craftable: Optional[int] = None
    transmute_cost: Optional[int] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None
    custom_icon: Optional[str] = None
    enchantment: Optional[EnchantmentSchema] = None

    model_config = ConfigDict(from_attributes=True)


class SkillSchema(BaseModel):
    id: str
    name: str
    skill_line: str
    morph: Optional[str] = None
    required_level: Optional[int] = None
    obtained: Optional[int] = None
    icon: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class BuildSkillAssignmentSchema(BaseModel):
    skill: SkillSchema
    bar: str
    position: int
    is_ultimate: Optional[int] = None


class ChampionPointsSchema(BaseModel):
    build_id: str
    warfare: Optional[str] = None
    fitness: Optional[str] = None
    craft: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class TraitSchema(BaseModel):
    id: str
    trait_type: str
    character_id: Optional[str] = None
    research_status: Optional[str] = None
    research_end_time: Optional[str] = None
    craftable: Optional[int] = None
    notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class SourceLinkSchema(BaseModel):
    id: str
    url: str
    site_name: Optional[str] = None
    author: Optional[str] = None
    patch_version: Optional[str] = None
    last_checked: Optional[str] = None
    notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

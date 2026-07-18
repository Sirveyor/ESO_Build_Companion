from sqlalchemy import Column, Integer, String, Text
from database import Base



class RefEnchantment(Base):
    __tablename__ = "ref_enchantments"
    id           = Column(String, primary_key=True)
    name         = Column(String, nullable=False)
    slot_type    = Column(String, nullable=False)  # Armor | Weapon | Jewelry
    effect       = Column(Text)
    essence_rune = Column(String)
    notes        = Column(Text)


class RefTrait(Base):
    __tablename__ = "ref_traits"
    id             = Column(String, primary_key=True)
    name           = Column(String, nullable=False)
    slot_type      = Column(String, nullable=False)  # Armor | Weapon | Jewelry
    effect         = Column(Text)
    trait_material = Column(String)
    notes          = Column(Text)


class RefMundusStone(Base):
    __tablename__ = "ref_mundus_stones"
    id        = Column(String, primary_key=True)
    name      = Column(String, nullable=False)
    effect    = Column(Text)
    stat_type = Column(String)
    location  = Column(Text)


class RefSkillLine(Base):
    __tablename__ = "ref_skill_lines"
    id         = Column(String, primary_key=True)
    name       = Column(String, nullable=False)
    # Class | Weapon | Armor | Guild | Alliance War | World | Racial | Craft
    category   = Column(String, nullable=False)
    # Populated only for Class lines (e.g. "Dragonknight")
    class_name = Column(String)


class RefSkill(Base):
    __tablename__ = "ref_skills"
    id            = Column(String, primary_key=True)
    skill_line_id = Column(String, nullable=False)  # FK to ref_skill_lines.id
    name          = Column(String, nullable=False)   # base skill name
    morph_1       = Column(String)                   # first morph option
    morph_2       = Column(String)                   # second morph option
    is_ultimate   = Column(Integer, default=0)


class RefResearchTrait(Base):
    __tablename__ = "ref_research_traits"
    id            = Column(String, primary_key=True)
    item_type     = Column(String, nullable=False)   # e.g. "Heavy Head", "Sword", "Necklace"
    trait_name    = Column(String, nullable=False)   # e.g. "Divines", "Powered", "Arcane"
    slot_category = Column(String, nullable=False)   # Armor | Weapon | Jewelry

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
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


class RefWeaponType(Base):
    __tablename__ = "ref_weapon_types"
    id         = Column(String, primary_key=True)
    name       = Column(String, nullable=False)
    parent_id  = Column(String)   # None = top-level category
    sort_order = Column(Integer, default=0)


class RefFood(Base):
    __tablename__ = "ref_food"
    id             = Column(String,  primary_key=True)
    name           = Column(String,  nullable=False)
    stat_bonuses   = Column(String)               # computed display string kept for BuildList compat
    food_type      = Column(String)               # Health | Magicka | Stamina | Health+Magicka | etc.
    dish_type      = Column(String)               # Meat | Fruit | Vegetable | Savoury | Ragout | Entremet | Gourmet
    ri             = Column(Integer, default=1)   # Recipe Improvement level required
    rq             = Column(Integer, default=1)   # Recipe quality tier
    food_level     = Column(Integer, default=1)   # Character level food scales to
    health_bonus   = Column(Integer, default=0)
    magicka_bonus  = Column(Integer, default=0)
    stamina_bonus  = Column(Integer, default=0)
    ing_meat       = Column(String)               # Protein ingredient type
    ing_fruit      = Column(String)               # Fruit ingredient type
    ing_veg        = Column(String)               # Vegetable ingredient type
    ing_med        = Column(String)               # Spice / medicine ingredient
    ing_impr       = Column(String)               # Improvement ingredient (Frost Mirriam)
    duration       = Column(Integer, default=35)  # Buff duration in minutes


class RefMotif(Base):
    __tablename__ = "ref_motifs"
    id           = Column(String, primary_key=True)
    name         = Column(String, nullable=False)  # Style name, e.g. "High Elf Style"
    motif_number = Column(Integer)                 # "Crafting Motif N" number
    category     = Column(String, nullable=False)  # Racial | Crafted | Crown Store | Dungeon/Trial | Overland | Event | PvP/Imperial City
    chapter      = Column(String)                  # None for single-book motifs; chapter name otherwise
    source       = Column(Text)                    # How/where the book or chapter is obtained


class RefFragmentSet(Base):
    __tablename__ = "ref_fragment_sets"
    id       = Column(String, primary_key=True)
    name     = Column(String, nullable=False)  # Collectible name, e.g. "Dwarven Theodolite"
    category = Column(String, nullable=False)  # Public Dungeon | Event | Prologue Quest | Tales of Tribute | Infinite Archive | Skill Style

    items = relationship("RefFragmentItem", back_populates="fragment_set", cascade="all, delete-orphan")


class RefFragmentItem(Base):
    __tablename__ = "ref_fragment_items"
    id      = Column(String, primary_key=True)
    set_id  = Column(String, ForeignKey("ref_fragment_sets.id"), nullable=False)
    name    = Column(String, nullable=False)  # Individual fragment/piece name
    source  = Column(Text)                    # Where/how this piece is obtained

    fragment_set = relationship("RefFragmentSet", back_populates="items")


class RefResearchTrait(Base):
    __tablename__ = "ref_research_traits"
    id            = Column(String, primary_key=True)
    item_type     = Column(String, nullable=False)   # e.g. "Heavy Head", "Sword", "Necklace"
    trait_name    = Column(String, nullable=False)   # e.g. "Divines", "Powered", "Arcane"
    slot_category = Column(String, nullable=False)   # Armor | Weapon | Jewelry

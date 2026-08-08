# These imports register every model with Base.metadata so create_all() builds all tables.
from database import Base, engine
import models.user          # noqa: F401
import models.character     # noqa: F401
import models.build         # noqa: F401
import models.gear_set      # noqa: F401
import models.gear_item     # noqa: F401
import models.skill         # noqa: F401
import models.trait         # noqa: F401
import models.source_link   # noqa: F401
import models.links         # noqa: F401
import models.champion_points  # noqa: F401
import models.build_skills     # noqa: F401
import models.reference        # noqa: F401
import models.recipe           # noqa: F401
import models.motif            # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)
    _migrate()
    _seed_reference()
    _seed_gear_sets()
    _seed_skill_lines()
    _seed_skills()
    _seed_research_traits()
    _seed_food()
    _seed_drinks()
    _seed_weapon_types()
    _seed_motifs()


def _migrate():
    """Safe incremental migrations for SQLite (ALTER TABLE ADD COLUMN is idempotent)."""
    from sqlalchemy import text
    migrations = [
        "ALTER TABLE traits ADD COLUMN character_id TEXT REFERENCES characters(id)",
        "ALTER TABLE characters ADD COLUMN alliance TEXT",
        "ALTER TABLE builds ADD COLUMN mundus_stone TEXT",
        "ALTER TABLE builds ADD COLUMN food_buff TEXT",
        "ALTER TABLE builds ADD COLUMN attr_health INTEGER",
        "ALTER TABLE builds ADD COLUMN attr_magicka INTEGER",
        "ALTER TABLE builds ADD COLUMN attr_stamina INTEGER",
        # ref_food extended columns
        "ALTER TABLE ref_food ADD COLUMN dish_type TEXT",
        "ALTER TABLE ref_food ADD COLUMN ri INTEGER",
        "ALTER TABLE ref_food ADD COLUMN rq INTEGER",
        "ALTER TABLE ref_food ADD COLUMN food_level INTEGER",
        "ALTER TABLE ref_food ADD COLUMN health_bonus INTEGER",
        "ALTER TABLE ref_food ADD COLUMN magicka_bonus INTEGER",
        "ALTER TABLE ref_food ADD COLUMN stamina_bonus INTEGER",
        "ALTER TABLE ref_food ADD COLUMN ing_meat TEXT",
        "ALTER TABLE ref_food ADD COLUMN ing_fruit TEXT",
        "ALTER TABLE ref_food ADD COLUMN ing_veg TEXT",
        "ALTER TABLE ref_food ADD COLUMN ing_med TEXT",
        "ALTER TABLE ref_food ADD COLUMN ing_impr TEXT",
        "ALTER TABLE ref_food ADD COLUMN duration INTEGER",
    ]
    with engine.connect() as conn:
        for sql in migrations:
            try:
                conn.execute(text(sql))
                conn.commit()
            except Exception:
                pass  # column already exists


def _seed_reference():
    """Populate ref_* tables with static ESO game data on first run. Skips if already seeded."""
    from sqlalchemy.orm import Session
    from models.reference import RefEnchantment, RefTrait, RefMundusStone

    with Session(engine) as db:
        # Skip if already seeded
        if db.query(RefEnchantment).count() > 0:
            return

        # ── Enchantments ──────────────────────────────────────────────────────
        # (id, name, slot_type, effect, essence_rune, notes)
        enchantments = [
            # Armor
            ("enc-arm-health",   "Glyph of Max Health",            "Armor",   "Adds Max Health to armor piece",                          "Oko",     None),
            ("enc-arm-magicka",  "Glyph of Max Magicka",           "Armor",   "Adds Max Magicka to armor piece",                         "Makderi", None),
            ("enc-arm-stamina",  "Glyph of Max Stamina",           "Armor",   "Adds Max Stamina to armor piece",                         "Deni",    None),
            ("enc-arm-physres",  "Glyph of Physical Resistance",   "Armor",   "Adds Physical Resistance to armor piece",                  "Rakeipa", None),
            ("enc-arm-spellres", "Glyph of Spell Resistance",      "Armor",   "Adds Spell Resistance to armor piece",                     "Haoko",   None),
            ("enc-arm-prismat",  "Glyph of Prismatic Defense",     "Armor",   "Adds Max Health, Magicka, and Stamina to armor piece",     "Makkoma", None),
            # Weapon
            ("enc-wep-fire",     "Glyph of Fire",                  "Weapon",  "Deals Fire Damage on hit",                                 "Rodo",    None),
            ("enc-wep-frost",    "Glyph of Frost",                 "Weapon",  "Deals Frost Damage on hit",                                "Dekeipa", None),
            ("enc-wep-shock",    "Glyph of Shock",                 "Weapon",  "Deals Shock Damage on hit",                                "Meip",    None),
            ("enc-wep-poison",   "Glyph of Poison",                "Weapon",  "Deals Poison Damage on hit",                               "Kuoko",   None),
            ("enc-wep-foul",     "Glyph of Foulness",              "Weapon",  "Deals Disease Damage on hit",                              "Okoma",   None),
            ("enc-wep-abshlth",  "Glyph of Absorb Health",         "Weapon",  "Deals Magic Damage on hit and restores your Health",       "Oko",     "Uses subtractive potency rune"),
            ("enc-wep-absmag",   "Glyph of Absorb Magicka",        "Weapon",  "Deals Magic Damage on hit and restores your Magicka",      "Makderi", "Uses subtractive potency rune"),
            ("enc-wep-absstam",  "Glyph of Absorb Stamina",        "Weapon",  "Deals Magic Damage on hit and restores your Stamina",      "Deni",    "Uses subtractive potency rune"),
            ("enc-wep-wpdmg",    "Glyph of Weapon Damage",         "Weapon",  "Increases your Weapon and Spell Damage",                   "Taderi",  None),
            ("enc-wep-harden",   "Glyph of Hardening",             "Weapon",  "Grants a Damage Shield on hit",                            "Rekura",  None),
            ("enc-wep-weak",     "Glyph of Weakening",             "Weapon",  "Reduces enemy Weapon and Spell Damage on hit",             "Kaderi",  None),
            ("enc-wep-crush",    "Glyph of Crushing",              "Weapon",  "Reduces enemy Physical and Spell Resistance on hit",       "Deteri",  None),
            ("enc-wep-dechlth",  "Glyph of Decrease Health",       "Weapon",  "Deals unresisted Oblivion Damage on hit",                  "Hanako",  None),
            ("enc-wep-prism",    "Glyph of Prismatic Onslaught",   "Weapon",  "Deals Magic, Frost, and Shock Damage on hit (bonus vs. Undead and Daedra)", "Makkoma", "Uses subtractive potency rune"),
            # Jewelry
            ("enc-jwl-physharm", "Glyph of Increase Physical Harm","Jewelry", "Increases Weapon Damage",                                  "Taderi",  None),
            ("enc-jwl-magharm",  "Glyph of Increase Magical Harm", "Jewelry", "Increases Spell Damage",                                   "Idode",   None),
            ("enc-jwl-hlthrc",   "Glyph of Health Recovery",       "Jewelry", "Increases Health Recovery",                                "Oko",     None),
            ("enc-jwl-magrc",    "Glyph of Magicka Recovery",      "Jewelry", "Increases Magicka Recovery",                               "Makderi", None),
            ("enc-jwl-stamrc",   "Glyph of Stamina Recovery",      "Jewelry", "Increases Stamina Recovery",                               "Deni",    None),
            ("enc-jwl-rspellc",  "Glyph of Reduce Spell Cost",     "Jewelry", "Reduces the cost of Magicka abilities",                    "Makderi", "Uses subtractive potency rune"),
            ("enc-jwl-rfeatc",   "Glyph of Reduce Feat Cost",      "Jewelry", "Reduces the cost of Stamina abilities",                    "Deni",    "Uses subtractive potency rune"),
            ("enc-jwl-rskillc",  "Glyph of Reduce Skill Cost",     "Jewelry", "Reduces the cost of all abilities",                        "Makkoma", "Uses subtractive potency rune"),
            ("enc-jwl-shield",   "Glyph of Shielding",             "Jewelry", "Reduces Block and Bash costs",                             "Rekura",  None),
            ("enc-jwl-bash",     "Glyph of Bashing",               "Jewelry", "Increases Bash damage",                                    "Deteri",  None),
            ("enc-jwl-dpharm",   "Glyph of Decrease Physical Harm","Jewelry", "Reduces Physical damage taken",                            "Rakeipa", "Uses subtractive potency rune"),
            ("enc-jwl-dsharm",   "Glyph of Decrease Spell Harm",   "Jewelry", "Reduces Spell damage taken",                               "Haoko",   "Uses subtractive potency rune"),
            ("enc-jwl-flameres", "Glyph of Flame Resist",          "Jewelry", "Increases Flame Resistance",                               "Rodo",    "Uses subtractive potency rune"),
            ("enc-jwl-frostres", "Glyph of Frost Resist",          "Jewelry", "Increases Frost Resistance",                               "Dekeipa", "Uses subtractive potency rune"),
            ("enc-jwl-shockres", "Glyph of Shock Resist",          "Jewelry", "Increases Shock Resistance",                               "Meip",    "Uses subtractive potency rune"),
            ("enc-jwl-poisonrs", "Glyph of Poison Resist",         "Jewelry", "Increases Poison Resistance",                              "Kuoko",   "Uses subtractive potency rune"),
            ("enc-jwl-disears",  "Glyph of Disease Resist",        "Jewelry", "Increases Disease Resistance",                             "Okoma",   "Uses subtractive potency rune"),
            ("enc-jwl-potres",   "Glyph of Potion Resist",         "Jewelry", "Reduces negative Potion effect durations",                 "Haoko",   "Uses subtractive potency rune"),
            ("enc-jwl-potbst",   "Glyph of Potion Boost",          "Jewelry", "Increases positive Potion effect durations",               "Haoko",   None),
            ("enc-jwl-prismrc",  "Glyph of Prismatic Recovery",    "Jewelry", "Restores Health, Magicka, and Stamina",                    "Makkoma", None),
        ]
        for e in enchantments:
            db.add(RefEnchantment(id=e[0], name=e[1], slot_type=e[2], effect=e[3], essence_rune=e[4], notes=e[5]))

        # ── Traits ────────────────────────────────────────────────────────────
        # (id, name, slot_type, effect, trait_material, notes)
        traits = [
            # Armor
            ("tr-arm-divines",  "Divines",      "Armor",   "Increases the effectiveness of Mundus Stones by 8%",                   "Sapphire",   None),
            ("tr-arm-infused",  "Infused",      "Armor",   "Increases Armor enchantment effect by 20% and reduces cooldown by 50%", "Bloodstone",  None),
            ("tr-arm-reinforc", "Reinforced",   "Armor",   "Increases the Armor value of this piece by 16%",                        "Ruby",        None),
            ("tr-arm-wfitted",  "Well-Fitted",  "Armor",   "Reduces the cost of Sprint by 3%",                                     "Almandine",  None),
            ("tr-arm-sturdy",   "Sturdy",       "Armor",   "Reduces the cost of Block by 3%",                                      "Quartz",     None),
            ("tr-arm-training", "Training",     "Armor",   "Increases experience gained from kills by 10%",                         "Carnelian",  None),
            ("tr-arm-intricate","Intricate",    "Armor",   "Increases Inspiration gained from deconstructing by 100%",              "Garnet",     "Cannot be researched; acquired from loot"),
            ("tr-arm-impenat",  "Impenetrable", "Armor",   "Increases Critical Resistance",                                         "Diamond",    None),
            ("tr-arm-prosp",    "Prosperous",   "Armor",   "Increases the amount of Gold found by 1%",                              "Citrine",    "Cannot be crafted; acquired from specific loot/vendors"),
            ("tr-arm-nirn",     "Nirnhoned",    "Armor",   "Increases Physical Resistance and Spell Resistance",                    "Nirncrux",   "Requires Potent Nirncrux; cannot be researched normally"),
            # Jewelry
            ("tr-jwl-arcane",   "Arcane",       "Jewelry", "Adds Max Magicka",                                                      "Cobalt",         None),
            ("tr-jwl-healthy",  "Healthy",      "Jewelry", "Adds Max Health",                                                       "Rose Quartz",    None),
            ("tr-jwl-robust",   "Robust",       "Jewelry", "Adds Max Stamina",                                                      "Turquoise",      None),
            ("tr-jwl-triune",   "Triune",       "Jewelry", "Adds Max Magicka, Health, and Stamina",                                 "Dawn-Prism",     None),
            ("tr-jwl-bloodth",  "Bloodthirsty", "Jewelry", "Increases your damage against enemies under 90% Health by 3%",          "Slaughterstone", None),
            ("tr-jwl-swift",    "Swift",         "Jewelry","Reduces the cost of Roll Dodge by 9% and Sprint by 18%",                "Gilding Wax",    None),
            ("tr-jwl-harmony",  "Harmony",      "Jewelry", "Increases the duration and power of your Synergies by 10%",             "Dibellite",      None),
            ("tr-jwl-protect",  "Protective",   "Jewelry", "Adds Physical Resistance and Spell Resistance",                         "Titanite",       None),
            ("tr-jwl-infused",  "Infused",      "Jewelry", "Increases Jewelry enchantment effect by 20%",                           "Aurbic Amber",   None),
            # Weapon
            ("tr-wep-precise",  "Precise",      "Weapon",  "Increases Weapon and Spell Critical",                                   "Emerald",    None),
            ("tr-wep-powered",  "Powered",      "Weapon",  "Reduces Skill cooldowns by 7%",                                         "Chysolite",  None),
            ("tr-wep-charged",  "Charged",      "Weapon",  "Increases chance to apply Status Effects by 110%",                      "Amethyst",   None),
            ("tr-wep-defend",   "Defending",    "Weapon",  "Increases Physical Resistance and Spell Resistance",                    "Turquoise",  None),
            ("tr-wep-sharp",    "Sharpened",    "Weapon",  "Increases Weapon and Spell Penetration",                                "Fire Opal",  None),
            ("tr-wep-decisive", "Decisive",     "Weapon",  "When you gain Ultimate you have a 33% chance to gain additional Ultimate","Citrine",  None),
            ("tr-wep-nirn",     "Nirnhoned",    "Weapon",  "Increases Weapon and Spell Damage",                                     "Nirncrux",   None),
            ("tr-wep-infused",  "Infused",      "Weapon",  "Increases Weapon enchantment effect by 30% and reduces cooldown by 50%","Jade",      None),
            ("tr-wep-training", "Training",     "Weapon",  "Increases experience gained from kills by 10%",                         "Carnelian",  None),
        ]
        for t in traits:
            db.add(RefTrait(id=t[0], name=t[1], slot_type=t[2], effect=t[3], trait_material=t[4], notes=t[5]))

        # ── Mundus Stones ─────────────────────────────────────────────────────
        # (id, name, effect, stat_type, location)
        stones = [
            ("mnd-apprentice", "The Apprentice", "Increases your Spell Damage",                                    "Spell Damage",            "Rivenspire (also in Coldhabour)"),
            ("mnd-atronach",   "The Atronach",   "Increases your Magicka Recovery",                                "Magicka Recovery",        "Eastmarch (also in Coldhabour)"),
            ("mnd-lady",       "The Lady",       "Increases your Physical Resistance and Spell Resistance",        "Resistance",              "Grahtwood (also in Coldhabour)"),
            ("mnd-lord",       "The Lord",       "Increases your Max Health",                                      "Max Health",              "Stormhaven (also in Coldhabour)"),
            ("mnd-lover",      "The Lover",      "Increases your Physical and Spell Penetration",                  "Penetration",             "Reaper's March (also in Coldhabour)"),
            ("mnd-mage",       "The Mage",       "Increases your Max Magicka",                                     "Max Magicka",             "Auridon (also in Coldhabour)"),
            ("mnd-ritual",     "The Ritual",     "Increases your Healing Done",                                    "Healing Done",            "Malabal Tor (also in Coldhabour)"),
            ("mnd-serpent",    "The Serpent",    "Increases your Stamina Recovery",                                "Stamina Recovery",        "Shadowfen (also in Coldhabour)"),
            ("mnd-shadow",     "The Shadow",     "Increases your Critical Damage Done and Critical Healing Done",  "Critical Damage",         "Bangkorai (also in Coldhabour)"),
            ("mnd-steed",      "The Steed",      "Increases your Movement Speed and Health Recovery",              "Movement Speed",          "Glenumbra (also in Coldhabour)"),
            ("mnd-thief",      "The Thief",      "Increases your Weapon and Spell Critical",                       "Weapon/Spell Critical",   "Khenarthi's Roost (also in Coldhabour)"),
            ("mnd-tower",      "The Tower",      "Increases your Max Stamina",                                     "Max Stamina",             "Alik'r Desert (also in Coldhabour)"),
            ("mnd-warrior",    "The Warrior",    "Increases your Weapon Damage",                                   "Weapon Damage",           "Daggerfall / Glenumbra (also in Coldhabour)"),
        ]
        for s in stones:
            db.add(RefMundusStone(id=s[0], name=s[1], effect=s[2], stat_type=s[3], location=s[4]))

        db.commit()


def _seed_gear_sets():
    """Populate gear_sets and set_bonuses from static ESO data. Skips sets that already exist."""
    from sqlalchemy.orm import Session
    from models.gear_set import GearSet, SetBonus
    from seed_gear_sets import GEAR_SETS
    import re

    def _slug(name):
        return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

    with Session(engine) as db:
        for (name, set_type, location, num_pieces, bonuses) in GEAR_SETS:
            if db.query(GearSet).filter_by(name=name).first():
                continue
            set_id = f"seed-{_slug(name)}"
            db.add(GearSet(
                id=set_id,
                name=name,
                set_type=set_type,
                location=location,
                num_pieces=num_pieces,
                notes="Seeded from ESO game data",
            ))
            for i, (pieces_required, bonus_description) in enumerate(bonuses):
                db.add(SetBonus(
                    id=f"{set_id}-b{i}",
                    set_id=set_id,
                    pieces_required=pieces_required,
                    bonus_description=bonus_description,
                ))
        db.commit()


def _seed_skill_lines():
    """Populate ref_skill_lines on first run. Skips if already seeded."""
    from sqlalchemy.orm import Session
    from models.reference import RefSkillLine
    from seed_skill_lines import SKILL_LINES

    with Session(engine) as db:
        if db.query(RefSkillLine).count() > 0:
            return
        for (id_, name, category, class_name) in SKILL_LINES:
            db.add(RefSkillLine(id=id_, name=name, category=category, class_name=class_name))
        db.commit()


def _seed_skills():
    """Populate ref_skills, inserting missing entries by ID. Handles moved/removed skills."""
    from sqlalchemy.orm import Session
    from models.reference import RefSkill
    from seed_skills import SKILLS

    # IDs removed from seed data that should be cleaned up from the database
    REMOVED_IDS = {"sk-nb-sha-2"}  # Veiled Strike moved from Shadow to Assassination

    with Session(engine) as db:
        for old_id in REMOVED_IDS:
            old = db.query(RefSkill).filter_by(id=old_id).first()
            if old:
                db.delete(old)
        for (id_, line_id, name, morph_1, morph_2, is_ult) in SKILLS:
            if not db.query(RefSkill).filter_by(id=id_).first():
                db.add(RefSkill(
                    id=id_, skill_line_id=line_id, name=name,
                    morph_1=morph_1, morph_2=morph_2, is_ultimate=is_ult,
                ))
        db.commit()


def _seed_weapon_types():
    """Populate ref_weapon_types with ESO weapon hierarchy. Skips if already seeded."""
    from sqlalchemy.orm import Session
    from models.reference import RefWeaponType
    from seed_weapon_types import WEAPON_TYPES

    with Session(engine) as db:
        if db.query(RefWeaponType).count() > 0:
            return
        for (id_, name, parent_id, sort_order) in WEAPON_TYPES:
            db.add(RefWeaponType(id=id_, name=name, parent_id=parent_id, sort_order=sort_order))
        db.commit()


def _seed_food():
    """Re-seed ref_food from the comprehensive RECIPES list, replacing legacy stub data."""
    import re
    from sqlalchemy.orm import Session
    from models.reference import RefFood
    from seed_food import RECIPES

    _FOOD_TYPE = {
        "Meat": "Health", "Fruit": "Magicka", "Vegetable": "Stamina",
        "Savoury": "Health+Magicka", "Ragout": "Health+Stamina",
        "Entremet": "Magicka+Stamina", "Gourmet": "All Stats",
        "Special": "Event",
        # Drinks
        "Alcohol":    "Health Recovery",
        "Tea":        "Magicka Recovery",
        "Tonic":      "Stamina Recovery",
        "Liqueur":    "Health+Magicka Recovery",
        "Tincture":   "Health+Stamina Recovery",
        "Cordial":    "Magicka+Stamina Recovery",
        "Distillate": "All Recovery",
    }

    _DRINK_TYPES = {"Alcohol", "Tea", "Tonic", "Liqueur", "Tincture", "Cordial", "Distillate"}

    def _slug(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    def _bonuses(h, m, s, dish=""):
        is_drink = dish in _DRINK_TYPES
        label = "Recovery" if is_drink else "Max"
        parts = []
        if h: parts.append(f"+{h} Health {label}")
        if m: parts.append(f"+{m} Magicka {label}")
        if s: parts.append(f"+{s} Stamina {label}")
        return ", ".join(parts)

    with Session(engine) as db:
        existing_ids = {r.id for r in db.query(RefFood.id).all()}
        for row in RECIPES:
            (name, ri, rq, lvl, dish, hp, mp, sp,
             i_meat, i_fruit, i_veg, i_med, i_impr, dur) = row
            rid = f"food-{_slug(name)}"
            if rid in existing_ids:
                continue
            db.add(RefFood(
                id=rid, name=name,
                stat_bonuses=_bonuses(hp, mp, sp, dish),
                food_type=_FOOD_TYPE.get(dish, dish),
                dish_type=dish, ri=ri, rq=rq, food_level=lvl,
                health_bonus=hp, magicka_bonus=mp, stamina_bonus=sp,
                ing_meat=i_meat, ing_fruit=i_fruit, ing_veg=i_veg,
                ing_med=i_med, ing_impr=i_impr, duration=dur,
            ))
        db.commit()


def _seed_drinks():
    """Seed standard provisioning drink recipes into ref_food. Skips existing rows by ID."""
    import re
    from sqlalchemy.orm import Session
    from models.reference import RefFood
    from seed_drinks import DRINKS

    _DRINK_FOOD_TYPE = {
        "Alcohol":    "Health Recovery",
        "Tea":        "Magicka Recovery",
        "Tonic":      "Stamina Recovery",
        "Liqueur":    "Health+Magicka Recovery",
        "Tincture":   "Health+Stamina Recovery",
        "Cordial":    "Magicka+Stamina Recovery",
        "Distillate": "All Recovery",
    }

    def _slug(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    def _bonuses(h, m, s):
        parts = []
        if h: parts.append(f"+{h} Health Recovery")
        if m: parts.append(f"+{m} Magicka Recovery")
        if s: parts.append(f"+{s} Stamina Recovery")
        return ", ".join(parts)

    with Session(engine) as db:
        existing_ids = {r.id for r in db.query(RefFood.id).all()}
        for row in DRINKS:
            (name, ri, rq, lvl, dish, hp, mp, sp,
             i_alco, i_tea, i_tonic, i_med, i_impr, dur) = row
            rid = f"food-{_slug(name)}"
            if rid in existing_ids:
                continue
            db.add(RefFood(
                id=rid, name=name,
                stat_bonuses=_bonuses(hp, mp, sp),
                food_type=_DRINK_FOOD_TYPE.get(dish, dish),
                dish_type=dish, ri=ri, rq=rq, food_level=lvl,
                health_bonus=hp, magicka_bonus=mp, stamina_bonus=sp,
                ing_meat=i_alco, ing_fruit=i_tea, ing_veg=i_tonic,
                ing_med=i_med, ing_impr=i_impr, duration=dur,
            ))
        db.commit()


def _seed_motifs():
    """Populate ref_motifs from MOTIFS. Skips entries that already exist by ID.

    Motifs marked chapters=True are farmed piecemeal, so each expands into one row
    per the 14 fixed gear-slot chapters rather than a single book-level row.
    """
    import re
    from sqlalchemy.orm import Session
    from models.reference import RefMotif
    from models.motif import LearnedMotif
    from seed_motifs import MOTIFS

    CHAPTER_NAMES = [
        "Axes", "Belt", "Boots", "Bows", "Chest", "Daggers", "Gloves",
        "Helmets", "Legs", "Maces", "Shields", "Shoulders", "Staves", "Swords",
    ]

    # IDs removed from seed data that should be cleaned up from the database
    REMOVED_IDS = {"motif-dremora-style"}  # reclassified from single-book to 14 chapters

    def _slug(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    with Session(engine) as db:
        for old_id in REMOVED_IDS:
            old = db.query(RefMotif).filter_by(id=old_id).first()
            if old:
                db.query(LearnedMotif).filter_by(motif_id=old_id).delete()
                db.delete(old)

        existing_ids = {r.id for r in db.query(RefMotif.id).all()}
        for (name, motif_number, category, chapters, source) in MOTIFS:
            base = f"motif-{_slug(name)}"
            entries = (
                [(f"{base}-{_slug(c)}", c) for c in CHAPTER_NAMES]
                if chapters else [(base, None)]
            )
            for mid, chapter in entries:
                if mid in existing_ids:
                    continue
                db.add(RefMotif(
                    id=mid, name=name, motif_number=motif_number,
                    category=category, chapter=chapter, source=source,
                ))
        db.commit()


def _seed_research_traits():
    """Populate ref_research_traits with all ESO researchable item/trait combinations. Skips if already seeded."""
    from sqlalchemy.orm import Session
    from models.reference import RefResearchTrait
    from seed_research_traits import RESEARCH_TRAITS

    with Session(engine) as db:
        if db.query(RefResearchTrait).count() > 0:
            return
        for (id_, item_type, trait_name, slot_category) in RESEARCH_TRAITS:
            db.add(RefResearchTrait(
                id=id_,
                item_type=item_type,
                trait_name=trait_name,
                slot_category=slot_category,
            ))
        db.commit()


if __name__ == "__main__":
    init_db()

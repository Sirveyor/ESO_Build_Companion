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


def init_db():
    Base.metadata.create_all(bind=engine)
    _migrate()
    _seed_reference()
    _seed_gear_sets()


def _migrate():
    """Safe incremental migrations for SQLite (ALTER TABLE ADD COLUMN is idempotent)."""
    from sqlalchemy import text
    migrations = [
        "ALTER TABLE traits ADD COLUMN character_id TEXT REFERENCES characters(id)",
        "ALTER TABLE characters ADD COLUMN alliance TEXT",
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


if __name__ == "__main__":
    init_db()

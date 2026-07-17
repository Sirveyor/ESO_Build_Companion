"""
ESO skill line seed data.
Format: (id, name, category, class_name)
class_name is None for all non-class skill lines.
"""

SKILL_LINES = [

    # ══════════════════════════════════════════════════════════════════════════
    # CLASS  — three skill lines per class
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-dk-ardent",    "Ardent Flame",          "Class", "Dragonknight"),
    ("sl-dk-draconic",  "Draconic Power",         "Class", "Dragonknight"),
    ("sl-dk-earthen",   "Earthen Heart",          "Class", "Dragonknight"),

    ("sl-sorc-daedric", "Daedric Summoning",      "Class", "Sorcerer"),
    ("sl-sorc-dark",    "Dark Magic",             "Class", "Sorcerer"),
    ("sl-sorc-storm",   "Storm Calling",          "Class", "Sorcerer"),

    ("sl-nb-assassin",  "Assassination",          "Class", "Nightblade"),
    ("sl-nb-shadow",    "Shadow",                 "Class", "Nightblade"),
    ("sl-nb-siphon",    "Siphoning",              "Class", "Nightblade"),

    ("sl-tp-aedric",    "Aedric Spear",           "Class", "Templar"),
    ("sl-tp-dawns",     "Dawn's Wrath",           "Class", "Templar"),
    ("sl-tp-restoring", "Restoring Light",        "Class", "Templar"),

    ("sl-wd-animal",    "Animal Companions",      "Class", "Warden"),
    ("sl-wd-green",     "Green Balance",          "Class", "Warden"),
    ("sl-wd-winter",    "Winter's Embrace",       "Class", "Warden"),

    ("sl-nc-grave",     "Grave Lord",             "Class", "Necromancer"),
    ("sl-nc-bone",      "Bone Tyrant",            "Class", "Necromancer"),
    ("sl-nc-living",    "Living Death",           "Class", "Necromancer"),

    ("sl-arc-herald",   "Herald of the Tome",     "Class", "Arcanist"),
    ("sl-arc-soldier",  "Soldier of Apocrypha",   "Class", "Arcanist"),
    ("sl-arc-curative", "Curative Runeforms",     "Class", "Arcanist"),

    # ══════════════════════════════════════════════════════════════════════════
    # WEAPON  — one line per weapon type
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-wep-2h",       "Two Handed",             "Weapon", None),
    ("sl-wep-1s",       "One Hand and Shield",    "Weapon", None),
    ("sl-wep-dw",       "Dual Wield",             "Weapon", None),
    ("sl-wep-bow",      "Bow",                    "Weapon", None),
    ("sl-wep-destro",   "Destruction Staff",      "Weapon", None),
    ("sl-wep-resto",    "Restoration Staff",      "Weapon", None),

    # ══════════════════════════════════════════════════════════════════════════
    # ARMOR  — one line per armor weight
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-arm-light",    "Light Armor",            "Armor", None),
    ("sl-arm-medium",   "Medium Armor",           "Armor", None),
    ("sl-arm-heavy",    "Heavy Armor",            "Armor", None),

    # ══════════════════════════════════════════════════════════════════════════
    # GUILD  — available to all characters; some require DLC
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-guild-fighters",  "Fighters Guild",      "Guild", None),
    ("sl-guild-mages",     "Mages Guild",         "Guild", None),
    ("sl-guild-undaunted", "Undaunted",           "Guild", None),
    ("sl-guild-thieves",   "Thieves Guild",       "Guild", None),  # Thieves Guild DLC
    ("sl-guild-db",        "Dark Brotherhood",    "Guild", None),  # Dark Brotherhood DLC
    ("sl-guild-psijic",    "Psijic Order",        "Guild", None),  # Summerset DLC

    # ══════════════════════════════════════════════════════════════════════════
    # ALLIANCE WAR  — unlocked by earning Alliance Points in Cyrodiil / BGs
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-aw-assault",   "Assault",                "Alliance War", None),
    ("sl-aw-support",   "Support",                "Alliance War", None),

    # ══════════════════════════════════════════════════════════════════════════
    # WORLD  — universal skill lines
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-world-soul",       "Soul Magic",         "World", None),
    ("sl-world-vampire",    "Vampire",            "World", None),
    ("sl-world-werewolf",   "Werewolf",           "World", None),
    ("sl-world-legerdemain","Legerdemain",        "World", None),

    # ══════════════════════════════════════════════════════════════════════════
    # RACIAL  — one line per playable race
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-race-altmer",   "Altmer",               "Racial", None),
    ("sl-race-bosmer",   "Bosmer",               "Racial", None),
    ("sl-race-khajiit",  "Khajiit",              "Racial", None),
    ("sl-race-breton",   "Breton",               "Racial", None),
    ("sl-race-orc",      "Orsimer",              "Racial", None),
    ("sl-race-redguard", "Redguard",             "Racial", None),
    ("sl-race-argonian", "Argonian",             "Racial", None),
    ("sl-race-dunmer",   "Dunmer",               "Racial", None),
    ("sl-race-nord",     "Nord",                 "Racial", None),
    ("sl-race-imperial", "Imperial",             "Racial", None),

    # ══════════════════════════════════════════════════════════════════════════
    # CRAFT  — leveled by crafting and researching
    # ══════════════════════════════════════════════════════════════════════════

    ("sl-craft-alchemy",    "Alchemy",            "Craft", None),
    ("sl-craft-blacksmith", "Blacksmithing",      "Craft", None),
    ("sl-craft-clothing",   "Clothing",           "Craft", None),
    ("sl-craft-enchanting", "Enchanting",         "Craft", None),
    ("sl-craft-jewelry",    "Jewelrycrafting",    "Craft", None),
    ("sl-craft-provision",  "Provisioning",       "Craft", None),
    ("sl-craft-woodwork",   "Woodworking",        "Craft", None),
]

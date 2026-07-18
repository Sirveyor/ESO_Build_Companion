"""
Common ESO provisioning buffs used in builds.
Format: (id, name, stat_bonuses, food_type)
  stat_bonuses — human-readable list of what the food gives
  food_type    — Magicka | Stamina | Hybrid | Tank | Healer | XP
"""

FOOD = [
    # ── Magicka DPS ──────────────────────────────────────────────────────────
    ("food-witchmother",     "Witchmother's Potent Brew",          "Max Magicka, Max Health, Magicka Recovery",                               "Magicka"),
    ("food-citrus-filet",    "Clockwork Citrus Filet",             "Max Magicka, Max Health, Magicka Recovery, Health Recovery",              "Magicka"),
    ("food-pickled-fish",    "Artaeum Pickled Fish Bowl",          "Max Magicka, Max Health",                                                 "Magicka"),
    ("food-sweetroll",       "Fragrant Honored Sweetroll",         "Max Magicka, Magicka Recovery",                                           "Magicka"),
    ("food-eyeball",         "Thousand-Year Pickled Eyeball",      "Max Health, Max Magicka",                                                 "Magicka"),

    # ── Stamina DPS ──────────────────────────────────────────────────────────
    ("food-dubious",         "Dubious Camoran Throne",             "Max Stamina, Max Health, Stamina Recovery",                               "Stamina"),
    ("food-longfin",         "Longfin Pasty with Mealy Plums",    "Max Health, Max Stamina, Stamina Recovery",                               "Stamina"),
    ("food-tripe-trifle",    "Orzorga's Tripe Trifle Pocket",     "Max Stamina, Max Health, Stamina Recovery",                               "Stamina"),
    ("food-skulls",          "Bewitched Sugar Skulls",             "Max Health, Max Stamina, Stamina Recovery, Magicka Recovery",             "Stamina"),
    ("food-netch-steak",     "Crispy Netch Steak with Cheddar",   "Max Health, Max Stamina",                                                 "Stamina"),
    ("food-pale-order",      "Pale Order's Golden Seabass",        "Max Stamina, Max Health, Stamina Recovery",                               "Stamina"),

    # ── Hybrid ───────────────────────────────────────────────────────────────
    ("food-ghastly-eye",     "Ghastly Eye Bowl",                   "Max Magicka, Max Stamina",                                                "Hybrid"),
    ("food-lava-foot",       "Lava Foot Soup-And-Saltrice",        "Max Stamina, Max Magicka",                                                "Hybrid"),
    ("food-solitude-salmon", "Solitude Salmon-Millet Soup",        "Max Stamina, Max Magicka, Stamina Recovery",                              "Hybrid"),
    ("food-garlic-cod",      "Garlic Cod with Potato Crust",       "Max Stamina, Max Magicka, Stamina Recovery",                              "Hybrid"),

    # ── Tank ─────────────────────────────────────────────────────────────────
    ("food-smoked-bear",     "Orzorga's Smoked Bear Haunch",      "Max Health, Stamina Recovery, Magicka Recovery",                          "Tank"),
    ("food-braised-rabbit",  "Braised Rabbit with Spring Vegetables", "Max Health, Magicka Recovery, Stamina Recovery",                       "Tank"),
    ("food-jewels",          "Jewels of Misrule",                  "Max Health, Health Recovery, Stamina Recovery",                           "Tank"),

    # ── Healer ───────────────────────────────────────────────────────────────
    ("food-bogbeast",        "Melon-Balled Bogbeast",              "Max Stamina, Stamina Recovery, Magicka Recovery",                         "Healer"),
    ("food-apricot-salad",   "Artaeum Takeaway Broth",             "Max Health, Health Recovery, Magicka Recovery",                           "Healer"),

    # ── XP / Utility ─────────────────────────────────────────────────────────
    ("food-psijic-ambrosia", "Psijic Ambrosia",                    "+50% Experience gain",                                                    "XP"),
    ("food-mythic-aetherial","Mythic Aetherial Ambrosia",          "+100% Experience gain",                                                   "XP"),
]

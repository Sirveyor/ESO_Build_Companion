"""
ESO weapon type hierarchy from weapon_types.txt.
Format: (id, name, parent_id, sort_order)
  parent_id = None for category headers (One Handed, Two Handed, etc.)
  Leaf nodes (parent_id is not None, or top-level with no children)
  are the specific types a player would select for a gear slot.
"""

WEAPON_TYPES = [
    # Category: One Handed
    ("wt-1",     "One Handed",         None,    10),
    ("wt-1-1",   "Dagger",             "wt-1",  11),
    ("wt-1-2",   "Mace",               "wt-1",  12),
    ("wt-1-3",   "Sword",              "wt-1",  13),
    ("wt-1-4",   "War Axe",            "wt-1",  14),
    ("wt-1-5",   "Shield",             "wt-1",  15),

    # Category: Two Handed
    ("wt-2",     "Two Handed",         None,    20),
    ("wt-2-1",   "Battle Axe",         "wt-2",  21),
    ("wt-2-2",   "Greatsword",         "wt-2",  22),
    ("wt-2-3",   "Maul",               "wt-2",  23),

    # Category: Destruction Staves
    ("wt-3",     "Destruction Staves", None,    30),
    ("wt-3-1",   "Flame Staff",        "wt-3",  31),
    ("wt-3-2",   "Frost Staff",        "wt-3",  32),
    ("wt-3-3",   "Lightning Staff",    "wt-3",  33),

    # Single-type categories (are themselves the leaf)
    ("wt-4",     "Restoration Staff",  None,    40),
    ("wt-5",     "Bow",                None,    50),
]

"""
ESO trait research combinations.
Every researchable item type × trait pairing — 324 total entries.
Format: (id, item_type, trait_name, slot_category)
  item_type     — e.g. "Heavy Head", "Sword", "Necklace"
  trait_name    — the trait being researched
  slot_category — "Armor" | "Weapon" | "Jewelry"
"""

_ARMOR_SLOTS = ['Head', 'Chest', 'Shoulders', 'Hands', 'Waist', 'Legs', 'Feet']
_ARMOR_WEIGHTS = ['Heavy', 'Medium', 'Light']
_ARMOR_TRAITS = [
    'Divines', 'Infused', 'Impenetrable', 'Reinforced',
    'Well-Fitted', 'Sturdy', 'Training', 'Exploration', 'Nirnhoned',
]

_WEAPON_TYPES = [
    # One Hand
    'Sword', 'Axe', 'Mace', 'Dagger',
    # Shield
    'Shield',
    # Two Hand
    'Greatsword', 'Battle Axe', 'Maul',
    # Ranged / Staff
    'Bow', 'Inferno Staff', 'Ice Staff', 'Lightning Staff', 'Restoration Staff',
]
_WEAPON_TRAITS = [
    'Powered', 'Charged', 'Precise', 'Infused', 'Defending',
    'Training', 'Sharpened', 'Weighted', 'Nirnhoned',
]

_JEWELRY_TYPES = ['Necklace', 'Ring']
_JEWELRY_TRAITS = [
    'Arcane', 'Healthy', 'Robust', 'Infused', 'Bloodthirsty',
    'Harmony', 'Protective', 'Swift', 'Triune',
]


def _slug(s):
    return s.lower().replace(' ', '-').replace("'", '').replace('.', '')


RESEARCH_TRAITS = []

for _weight in _ARMOR_WEIGHTS:
    for _slot in _ARMOR_SLOTS:
        for _trait in _ARMOR_TRAITS:
            RESEARCH_TRAITS.append((
                f"rt-{_slug(_weight)}-{_slug(_slot)}-{_slug(_trait)}",
                f"{_weight} {_slot}",
                _trait,
                "Armor",
            ))

for _wtype in _WEAPON_TYPES:
    for _trait in _WEAPON_TRAITS:
        RESEARCH_TRAITS.append((
            f"rt-{_slug(_wtype)}-{_slug(_trait)}",
            _wtype,
            _trait,
            "Weapon",
        ))

for _jtype in _JEWELRY_TYPES:
    for _trait in _JEWELRY_TRAITS:
        RESEARCH_TRAITS.append((
            f"rt-{_slug(_jtype)}-{_slug(_trait)}",
            _jtype,
            _trait,
            "Jewelry",
        ))

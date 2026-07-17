"""
ESO gear set seed data — CP160 Legendary quality, approximate values.
Bonus numbers may vary slightly between patches. Use the UESP scraper
to import additional sets or correct specific values.

Format: (name, set_type, location, num_pieces, [(pieces_required, bonus_description)])
"""

GEAR_SETS = [

    # ══════════════════════════════════════════════════════════════════════════
    # CRAFTED  (require trait research; craftable at any station of that type)
    # ══════════════════════════════════════════════════════════════════════════

    ("Armor of the Trainee", "Crafted", "Any crafting station (0 traits)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Adds 1096 Max Health, 1096 Max Magicka, and 1096 Max Stamina"),
    ]),
    ("Fortified Brass", "Crafted", "Any crafting station (3 traits)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "Adds 4936 Spell Resistance"),
    ]),
    ("Seducer", "Crafted", "Any crafting station (4 traits)", 5, [
        (2, "Reduces the cost of your Magicka abilities by 8%"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Reduces the cost of your Magicka abilities by 8%"),
        (5, "Reduces the cost of your Magicka abilities by 8%"),
    ]),
    ("Willow's Path", "Crafted", "Any crafting station (4 traits)", 5, [
        (2, "Adds 1206 Stamina Recovery"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "Adds 1206 Stamina Recovery"),
    ]),
    ("Law of Julianos", "Crafted", "Any crafting station (5 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 833 Weapon and Spell Critical"),
        (4, "Adds 833 Weapon and Spell Critical"),
        (5, "Adds 833 Weapon and Spell Critical"),
    ]),
    ("Hunding's Rage", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Adds 948 Weapon and Spell Damage"),
    ]),
    ("Night Mother's Gaze", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Reduces the Physical Resistance of enemies you damage by 3277"),
    ]),
    ("Magnus' Gift", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you take damage, you have a 10% chance to restore 4948 Magicka. This effect can occur once every 5 seconds."),
    ]),
    ("Torug's Pact", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Reduces the cooldown of your weapon enchantments by 50%"),
        (5, "Reduces the cooldown of your weapon enchantments by 50% and increases their damage by 30%"),
    ]),
    ("Alessia's Bulwark", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Health"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases your Block mitigation by 10%"),
    ]),
    ("Hist Bark", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Reduces the cost of Roll Dodge by 14%"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "When you activate an Evasion ability, you gain 5948 Armor for 5 seconds."),
    ]),
    ("Clever Alchemist", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you drink a potion, you gain 1854 Weapon and Spell Damage for 15 seconds."),
    ]),
    ("Eternal Hunt", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage with a Bow ability, you gain Major Evasion for 5 seconds, reducing damage from area attacks by 20%."),
    ]),
    ("Shacklebreaker", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Adds 3289 Max Stamina and 3289 Max Magicka"),
    ]),
    ("Innate Axiom", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases the damage of your non-class abilities by 1490"),
    ]),
    ("Song of Lamae", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 1096 Max Health"),
        (5, "When you take damage, you have a 50% chance to create a circle of necrotic energy for 5 seconds that damages nearby enemies."),
    ]),
    ("Oblivion's Foe", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Dealing damage to a Daedra or Undead has a 10% chance to invoke Meridia's Wrath, dealing Magic Damage to nearby enemies. This effect can occur once every 10 seconds."),
    ]),
    ("Kvatch Gladiator", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Adds 1528 Weapon and Spell Damage"),
    ]),
    ("Vampire's Kiss", "Crafted", "Any crafting station (6 traits)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal melee damage, you restore 975 Health. This effect can occur once every 1 second."),
    ]),
    ("Morkuldin", "Crafted", "Any crafting station (7 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage with a weapon ability, you have a 10% chance to summon an animated weapon to fight at your side for 30 seconds. This effect can occur once every 15 seconds."),
    ]),
    ("Kagrenac's Hope", "Crafted", "Any crafting station (7 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Reduces the time to revive a dead ally by 25%. When you successfully revive an ally, you restore Health, Magicka, and Stamina to nearby allies."),
    ]),
    ("Orgnum's Scales", "Crafted", "Any crafting station (8 traits)", 5, [
        (2, "Adds 1206 Magicka Recovery"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 1206 Magicka Recovery"),
        (5, "While your Magicka is above 50%, you gain Minor Mending, increasing your Healing Done by 8%."),
    ]),
    ("Pelinal's Aptitude", "Crafted", "Any crafting station (8 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Your Weapon and Spell Damage are equivalent to whichever is higher between the two."),
    ]),
    ("Twice-Born Star", "Crafted", "Any crafting station (9 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "You can benefit from two different Mundus Stone blessings simultaneously."),
    ]),
    ("Eternal Warrior", "Crafted", "Any crafting station (9 traits)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1096 Max Health"),
        (5, "When you die, you are resurrected with 50% of your Max Health after 4 seconds. This effect can occur once every 10 minutes."),
    ]),
    ("Aetherial Ascension", "Crafted", "Any crafting station (9 traits)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 1206 Magicka Recovery"),
        (4, "Adds 1096 Max Magicka"),
        (5, "You gain up to 1528 Weapon and Spell Damage based on your missing Magicka."),
    ]),
    ("Whitestrake's Retribution", "Crafted", "Any crafting station (9 traits)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Health"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Completing PvP objectives grants stacks of Whitestrake's Valor. At 5 stacks, they are consumed for Alliance Points and resources."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # MONSTER SETS  (Head from Veteran dungeon final boss; Shoulders from
    #                Undaunted Tribute Chests or daily Undaunted quests)
    # ══════════════════════════════════════════════════════════════════════════

    ("Velidreth", "Monster", "Darkshade Caverns II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal damage, you spawn up to 2 disease spores at the enemy's location for 6 seconds that explode for Disease Damage when triggered. This effect can occur once every 5 seconds."),
    ]),
    ("Ilambris", "Monster", "Crypts of Hearts I (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal damage with a Lightning or Fire ability, you have a 33% chance to spawn a meteor of that element dealing heavy Elemental Damage. This effect can occur once every 5 seconds."),
    ]),
    ("Selene", "Monster", "Selene's Web (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal melee damage, you have a 6% chance to summon Selene's bear to charge your enemy for Physical Damage. This effect can occur once every 5 seconds."),
    ]),
    ("Slimecraw", "Monster", "Wayrest Sewers I (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1528 Weapon and Spell Critical"),
        (2, "Gain Minor Berserk at all times, increasing your damage done by 5%."),
    ]),
    ("Kra'gh", "Monster", "Fungal Grotto I (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "Increases your Weapon and Spell Penetration by 4746."),
    ]),
    ("Pirate Skeleton", "Monster", "Blackheart Haven (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you take damage, you have a 10% chance to gain a Damage Shield that absorbs up to 20000 damage for 6 seconds, then explodes for Physical Damage to nearby enemies. This effect can occur once every 15 seconds."),
    ]),
    ("Grothdarr", "Monster", "Vaults of Madness (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal damage, you have a 10% chance to surround yourself in a scorching aura for 5 seconds, dealing Flame Damage to nearby enemies per second. This effect can occur once every 10 seconds."),
    ]),
    ("Valkyn Skoria", "Monster", "City of Ash II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal a Critical Strike, you have a 20% chance to call a meteor from the sky at the target's location, dealing Flame Damage and knocking them off balance. This effect can occur once every 10 seconds."),
    ]),
    ("Iceheart", "Monster", "Direfrost Keep (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal Critical Damage, you have a 20% chance to encase yourself in ice for 5 seconds, granting a Damage Shield and freezing nearby enemies, then exploding for Frost Damage. This effect can occur once every 10 seconds."),
    ]),
    ("Bloodspawn", "Monster", "Spindleclutch II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you take damage, you have a 6% chance to recover 26 Ultimate. This effect can occur once every 1 second."),
    ]),
    ("Shadowrend", "Monster", "Blessed Crucible (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal damage, you have a 10% chance to summon a shadow Render for 15 seconds that deals Magic Damage to nearby enemies and reduces their Weapon and Spell Damage. This effect can occur once every 10 seconds."),
    ]),
    ("Sentinel of Rkugamz", "Monster", "Ruins of Mazzatun (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you cast a Restoration Staff ability, you have a 10% chance to summon a healing automaton for 15 seconds that restores Health and Stamina to nearby allies per second. This effect can occur once every 10 seconds."),
    ]),
    ("Engine Guardian", "Monster", "Darkshade Caverns II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you use a class ability, you have a 10% chance to restore Magicka, Stamina, or Health to yourself. This effect can occur once every 5 seconds."),
    ]),
    ("Lord Warden", "Monster", "Imperial City Prison (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you take damage, you have a 20% chance to summon a shadow orb for 10 seconds that grants Major Resolve to you and nearby allies. This effect can occur once every 10 seconds."),
    ]),
    ("The Troll King", "Monster", "Elden Hollow II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you take damage, you have a 20% chance to restore Health per second for 5 seconds to you and all nearby allies. This effect can occur once every 5 seconds."),
    ]),
    ("Mighty Chudan", "Monster", "Ruins of Mazzatun (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you take damage, you have a 20% chance to gain Major Ward and Major Resolve for 8 seconds, increasing your Physical and Spell Resistance by 5948. This effect can occur once every 10 seconds."),
    ]),
    ("Thurvokun", "Monster", "Fang Lair (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When an enemy you've Poisoned attacks you, they become Diseased and deal Disease Damage to nearby enemies. This effect can occur once every 5 seconds."),
    ]),
    ("Swarm Mother", "Monster", "Spindleclutch I (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you cast an ability that costs Magicka, you pull all enemies within 8 meters to you. This effect can occur once every 8 seconds."),
    ]),
    ("Spawn of Mephala", "Monster", "Tempest Island (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal damage, you have a 10% chance to fire a web at the enemy dealing Poison Damage per second and reducing their Movement Speed. This effect can occur once every 10 seconds."),
    ]),
    ("Tremorscale", "Monster", "Volenfell (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you taunt an enemy, you cause a seismic tremor beneath them for 7 seconds that reduces their Physical Resistance and deals Physical Damage per second to nearby enemies. This effect can occur once every 15 seconds."),
    ]),
    ("Bogdan the Nightflame", "Monster", "Elden Hollow I (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Health"),
        (2, "When you deal damage, you have a 10% chance to summon a totem for 10 seconds that heals you and nearby allies per second. This effect can occur once every 15 seconds."),
    ]),
    ("Domihaus", "Monster", "Falkreath Hold (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Stamina or Max Magicka (whichever is higher)"),
        (2, "When you deal damage, you have a 10% chance to summon a Flame Ring and a Stone Ring for 10 seconds. The Flame Ring deals Flame Damage to enemies inside; the Stone Ring grants Physical and Spell Resistance to allies inside. This effect can occur once every 25 seconds."),
    ]),
    ("Scourge Harvester", "Monster", "Wayrest Sewers II (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal damage, you have a 10% chance to drain nearby enemies of Magicka per second for 4 seconds. This effect can occur once every 15 seconds."),
    ]),
    ("Stone Keeper", "Monster", "Frostvault (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you use a fully-charged Heavy Attack, you restore Health, Magicka, and Stamina. This effect can occur once every 5 seconds."),
    ]),
    ("Molag Kena", "Monster", "White-Gold Tower (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal damage with a Light or Heavy Attack, you gain 450 Weapon and Spell Damage for 4 seconds. After gaining this bonus 5 times you gain Empower for 10 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Balorgh", "Monster", "March of Sacrifices (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you activate your Ultimate ability, you gain Weapon and Spell Damage equal to the Ultimate's cost for 15 seconds. This effect can occur once every 15 seconds."),
    ]),
    ("Encratis's Behemoth", "Monster", "Black Drake Villa (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you deal Flame Damage, you apply Engulf to the enemy for 5 seconds, reducing their Flame Resistance and healing you. This effect can occur once every 1 second."),
    ]),
    ("Maarselok", "Monster", "Lair of Maarselok (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 129 Weapon and Spell Damage"),
        (2, "When you deal damage over time, you apply Corruption to the enemy for 10 seconds. Corrupted enemies spread Corruption to nearby enemies. Corruption reduces enemies' Max Health and deals Magic Damage per second. This effect can occur once every 15 seconds."),
    ]),
    ("Mother Ciannait", "Monster", "Unhallowed Grave (Veteran) / Undaunted Chest", 2, [
        (1, "Adds 1096 Max Magicka"),
        (2, "When you cast a Barrier ability, you and up to 5 group members gain a Ward for 6 seconds. This effect can occur once every 10 seconds."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # OVERLAND  (drop from world bosses, delve bosses, treasure chests,
    #            and zone enemies — one set per weight per zone)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Ebonheart Pact base zones ─────────────────────────────────────────────
    ("Armor of Truth", "Overland", "Stonefalls (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 4936 Spell Resistance"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Adds 129 Weapon and Spell Damage and reduces the cost of Restoration Staff abilities by 15%."),
    ]),
    ("Shalk Exoskeleton", "Overland", "Stonefalls (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you take damage, you have a 10% chance to gain Major Ward and Major Resolve for 5 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Mother's Sorrow", "Overland", "Deshaan (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Adds 1333 Weapon and Spell Critical"),
    ]),
    ("Plague Doctor", "Overland", "Rivenspire (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "Adds 4727 Max Health"),
    ]),
    ("Swamp Raider", "Overland", "Shadowfen (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases your Poison and Disease Damage by 15%."),
    ]),
    ("Ice Furnace", "Overland", "Eastmarch (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you deal Frost Damage, you deal additional Flame Damage to the target. This effect can occur once every 1 second."),
    ]),
    ("Morag Tong", "Overland", "Eastmarch (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal a Critical Strike, you apply a Poison to the target that deals Poison Damage over 6 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Leki's Focus", "Overland", "The Rift (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases your Light and Heavy Attack damage by 15%."),
    ]),
    ("Trinimac's Valor", "Overland", "The Rift (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal a Critical Strike, you and nearby group members gain Minor Berserk for 10 seconds, increasing damage by 5%."),
    ]),
    # ── Daggerfall Covenant base zones ───────────────────────────────────────
    ("Bloodthorn's Touch", "Overland", "Glenumbra (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal Critical Damage, you set the target On Fire for 4 seconds. This effect can occur once every 5 seconds."),
    ]),
    ("Death's Wind", "Overland", "Glenumbra (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you take damage that reduces your Health below 50%, you release a violent gust of wind, knocking nearby enemies back and granting you Major Protection for 3 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Hist Sap", "Overland", "Stormhaven (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you activate a channeled or cast-time ability, you gain Minor Vitality for 3 seconds, increasing Healing Received by 8%."),
    ]),
    ("Knight Slayer", "Overland", "Bangkorai (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage to a blocking enemy, you restore 1476 Stamina and reduce their Block effectiveness by 36%. This effect can occur once every 1 second."),
    ]),
    ("Briarheart", "Overland", "Wrothgar (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "When you deal a Critical Strike, you gain 450 Weapon and Spell Damage for 10 seconds. While this bonus is active, your Critical Strikes heal you for 2210 Health. This effect can occur once every 5 seconds."),
    ]),
    ("Hircine's Veneer", "Overland", "Alik'r Desert (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases the damage of your Fighters Guild abilities by 10% and reduces their costs by 10%."),
    ]),
    # ── Aldmeri Dominion base zones ───────────────────────────────────────────
    ("Twilight's Embrace", "Overland", "Auridon (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 1206 Magicka Recovery"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you heal an ally, you have a 10% chance to grant them Major Ward and Major Resolve for 6 seconds. This effect can occur once every 5 seconds."),
    ]),
    ("Dreamer's Mantle", "Overland", "Auridon (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 657 Weapon and Spell Critical"),
        (5, "When you deal damage with a Light Attack, you gain 190 Weapon and Spell Damage for 3 seconds. This effect can occur once every 1 second and stacks up to 4 times."),
    ]),
    ("Wilderqueen's Arch", "Overland", "Grahtwood (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you cast an ability that costs Magicka, you gain a stack of Nature's Bounty for 10 seconds, up to 5 stacks. At 5 stacks, they are consumed to restore Magicka."),
    ]),
    ("Durok's Bane", "Overland", "Greenshade (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "Reduces the Healing enemies near you receive by 20%."),
    ]),
    ("Swamp Raider (Malabal Tor)", "Overland", "Malabal Tor (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases your Poison and Disease damage by 15%."),
    ]),
    # ── DLC overland zones ────────────────────────────────────────────────────
    ("Mechanical Acuity", "Overland", "Clockwork City (world bosses, chests, enemies)", 5, [
        (2, "Adds 657 Weapon and Spell Critical"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 657 Weapon and Spell Critical"),
        (5, "After casting an ability, you gain up to 2499 Weapon and Spell Critical for 6 seconds based on abilities cast in the last 6 seconds."),
    ]),
    ("Burning Spellweave", "Overland", "Vvardenfell (world bosses, chests, enemies)", 5, [
        (2, "Adds 657 Weapon and Spell Critical"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 657 Weapon and Spell Critical"),
        (5, "When you deal Fire Damage, you have a 10% chance to gain 636 Weapon and Spell Damage for 10 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Viper's Sting", "Overland", "Murkmire (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Dealing damage with a Poison or Disease ability causes your other Poison and Disease abilities to deal 15% more damage for 10 seconds."),
    ]),
    ("Livewire", "Overland", "Elsweyr (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal Shock Damage, you have a chance to send a lightning bolt to a nearby enemy dealing Shock Damage. This effect can occur once every 5 seconds."),
    ]),
    ("Adept Rider", "Overland", "Western Skyrim (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Reduces your damage taken while mounted and increases your mounted speed."),
    ]),
    ("Shalidor's Curse", "Overland", "Western Skyrim (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 1206 Magicka Recovery"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal damage, you have a 10% chance to curse the enemy to deal Magic Damage to themselves when they deal damage for 5 seconds. This effect can occur once every 20 seconds."),
    ]),
    ("Arkasis's Genius", "Overland", "The Reach (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you apply a status effect to an enemy, you create a volatile concoction at their location that explodes after 3 seconds for Magic Damage. This effect can occur once every 10 seconds."),
    ]),
    ("Combined Victor", "Overland", "Blackwood (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 1206 Stamina Recovery"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage, you have a 10% chance to call for aid, healing you and nearby allies. This effect can occur once every 10 seconds."),
    ]),
    ("Coral Riptide", "Overland", "High Isle (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage with a Bash, Light, or Heavy Attack you summon a wave of water that deals Frost Damage. This effect can occur once every 4 seconds."),
    ]),
    ("Mara's Balm", "Overland", "High Isle (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1206 Health Recovery"),
        (4, "Adds 1096 Max Health"),
        (5, "Negative effects applied to you are reduced in duration by 50%."),
    ]),
    ("Azureblight Reaper", "Overland", "Necrom (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal damage with a Damage over Time effect, you infest the enemy with Blight for 10 seconds. When an infested enemy dies, the Blight explodes, dealing Magic Damage to nearby enemies."),
    ]),
    ("Rattlecage", "Overland", "Coldharbour (world bosses, chests, enemies)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Gain Major Sorcery at all times, increasing your Spell Damage by 20%."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # DUNGEON  (drop from specific dungeon bosses and treasure chests)
    # ══════════════════════════════════════════════════════════════════════════

    ("Medusa", "Dungeon", "Arx Corinium", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 657 Weapon and Spell Critical"),
        (5, "Gain Major Prophecy and Major Sorcery at all times, increasing your Weapon/Spell Critical and Weapon/Spell Damage by 20%."),
    ]),
    ("Nerien'eth", "Dungeon", "Crypt of Hearts II", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal a Critical Strike, you have a 10% chance to summon a lich that casts a Destruction Staff ability at your target. This effect can occur once every 10 seconds."),
    ]),
    ("Caluurion's Legacy", "Dungeon", "Icereach", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 657 Weapon and Spell Critical"),
        (5, "When you deal a Critical Strike with a single-target ability, you fire a bolt of Fire, Frost, Shock, or Disease at your target dealing Elemental Damage and applying a 7-second debuff. This effect can occur once every 5 seconds."),
    ]),
    ("Tzogvin's Warband", "Dungeon", "Frostvault", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "When you deal a Critical Strike, you gain a stack of Precision for 5 seconds, up to 5 stacks. At max stacks, you gain Minor Force, increasing your Critical Damage by 10%."),
    ]),
    ("Blooddrinker", "Dungeon", "Fang Lair", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases your damage done with Bleed abilities by 15%."),
    ]),
    ("Hollowfang Thirst", "Dungeon", "Depths of Malatar", 5, [
        (2, "Adds 1206 Magicka Recovery"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 1206 Magicka Recovery"),
        (5, "When you deal damage, you have a 10% chance to feast on your enemy, restoring Magicka to yourself. This effect can occur once every 5 seconds and benefits from the Vampire passive Dark Stalker."),
    ]),
    ("Kinras' Wrath", "Dungeon", "Stone Garden", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal damage with a Light or Heavy Attack, you gain a stack of Seething Fury for 5 seconds, up to 5 stacks. At max stacks, you release an explosion of fire dealing Flame Damage and gaining Major Berserk for 5 seconds."),
    ]),
    ("Turning Tide", "Dungeon", "Coral Aerie", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage to enemies affected by a negative effect you applied, you restore Stamina. This effect can occur once every 1 second."),
    ]),
    ("Crimson Oath's Rive", "Dungeon", "Shipwright's Regret", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you taunt an enemy, you restore Health and grant nearby allies a Damage Shield for 3 seconds. This effect can occur once every 2 seconds."),
    ]),
    ("Ansuul's Torment", "Dungeon", "Bal Sunnar", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Dealing damage applies a stack of Sanity's Burden on the enemy for 5 seconds. At 5 stacks, a shockwave erupts dealing Magic Damage to the enemy and nearby enemies."),
    ]),
    ("Deadly Strike", "Arena", "Vateshran Hollows (Perfected version available)", 5, [
        (2, "Adds 129 Weapon and Spell Damage"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Increases your damage done with Damage over Time and channeled abilities by 15%."),
    ]),
    ("Perfected Deadly Strike", "Arena", "Vateshran Hollows (Veteran)", 5, [
        (2, "Adds 129 Weapon and Spell Damage"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Increases your damage done with Damage over Time and channeled abilities by 15%. Adds 1096 Max Stamina (Perfected bonus)."),
    ]),
    ("Crushing Wall", "Arena", "Maelstrom Arena (Perfected version available)", 5, [
        (2, "Adds 129 Weapon and Spell Damage"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Increases your damage against enemies in your Wall of Elements by 1190."),
    ]),
    ("Perfected Crushing Wall", "Arena", "Maelstrom Arena (Veteran)", 5, [
        (2, "Adds 129 Weapon and Spell Damage"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "Increases your damage against enemies in your Wall of Elements by 1190. Adds 1096 Max Magicka (Perfected bonus)."),
    ]),
    ("Titanic Cleave", "Arena", "Dragonstar Arena (Veteran)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Increases the radius of your Area of Effect abilities by 2 meters."),
    ]),
    ("Combat Physician", "Dungeon", "Blackrose Prison", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 1096 Max Health"),
        (5, "When you heal yourself or an ally who is below 50% Health, you grant them a Damage Shield for 3 seconds that absorbs damage. This effect can occur once every 6 seconds per target."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # TRIAL  (drop from 12-player trial encounters — Normal and Veteran)
    # ══════════════════════════════════════════════════════════════════════════

    ("Spell Power Cure", "Trial", "Aetherian Archive (Normal/Veteran)", 5, [
        (2, "Adds 129 Weapon and Spell Damage"),
        (3, "Adds 1096 Max Magicka"),
        (4, "Adds 129 Weapon and Spell Damage"),
        (5, "When you heal yourself or an ally with a Restoration Staff ability, you grant up to 6 nearby allies Minor Heroism for 8 seconds, increasing Ultimate gain by 1 per second."),
    ]),
    ("Scathing Mage", "Trial", "Aetherian Archive (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal a Critical Strike, you increase your Weapon and Spell Damage by 490 for 5 seconds. This effect can occur once every 1 second."),
    ]),
    ("Roar of Alkosh", "Trial", "Maw of Lorkhaj (Normal/Veteran)", 5, [
        (2, "Adds 1206 Stamina Recovery"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "When you activate a Synergy, you send a shockwave from your position that reduces the Physical and Spell Resistance of enemies hit by 3010 for 15 seconds. This effect can occur once every 10 seconds."),
    ]),
    ("Ebon Armory", "Trial", "Maw of Lorkhaj (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "Increases the Max Health of you and your group members within 28 meters by 1000."),
    ]),
    ("Vicious Ophidian", "Trial", "Maw of Lorkhaj (Normal/Veteran)", 5, [
        (2, "Adds 1206 Stamina Recovery"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "When you deal damage, you have a 15% chance to generate 3 Ultimate and restore Stamina. This effect can occur once every 1 second."),
    ]),
    ("Symphony of Blades", "Trial", "Halls of Fabrication (Normal/Veteran)", 5, [
        (2, "Adds 1206 Stamina Recovery"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1206 Magicka Recovery"),
        (5, "When your Ultimate ability is fully charged, you share 30 of your Ultimate with the group member with the lowest Ultimate. This effect can occur once every 5 seconds."),
    ]),
    ("Arms of Relequen", "Trial", "Halls of Fabrication (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "Light and Heavy Attacks apply a stack of Winds of Relequen for 5 seconds, up to 5 stacks. Each stack deals 145 Physical Damage per second. At max stacks you also gain Minor Slayer, increasing your damage against Dungeon, Trial, and Arena monsters by 5%."),
    ]),
    ("Siroria", "Trial", "Cloudrest (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you remain stationary, you generate a stack of Siroria's Boon every 1 second, up to 10 stacks. Each stack increases your Spell Damage by 45. Moving removes one stack per second."),
    ]),
    ("Infallible Aether", "Trial", "Cloudrest (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Light and Heavy Attacks apply Minor Vulnerability to the enemy for 5 seconds, increasing their damage taken by 5%."),
    ]),
    ("Bahsei's Mania", "Trial", "Rockgrove (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Dealing damage converts up to 30% of your current Magicka into up to 1528 additional Weapon and Spell Damage, based on how much Magicka you are missing."),
    ]),
    ("Whorl of the Depths", "Trial", "Rockgrove (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage with a fully-charged Heavy Attack, you create a whirlpool for 10 seconds that deals Magic Damage to nearby enemies per second and heals the lowest-Health ally in the whirlpool. This effect can occur once every 15 seconds."),
    ]),
    ("Powerful Assault", "Trial", "Sanity's Edge (Normal/Veteran)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you use a fully-charged Heavy Attack, you grant Minor Force to nearby group members for 10 seconds, increasing Critical Damage by 10%."),
    ]),
    ("Drake's Rush", "Trial", "Kyne's Aegis (Normal/Veteran)", 5, [
        (2, "Adds 1206 Stamina Recovery"),
        (3, "Adds 1096 Max Stamina"),
        (4, "Adds 1206 Stamina Recovery"),
        (5, "When you taunt an enemy, you gain a persistent stack of Drake's Rush for 1 hour. Each stack increases your Physical and Spell Resistance by 260, up to 10 stacks. When you reach 10 stacks, they are consumed to grant you a Damage Shield."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # MYTHIC  (single-piece sets from Antiquities — Lead Fragments in DLC zones)
    # ══════════════════════════════════════════════════════════════════════════

    ("Oakensoul Ring", "Mythic", "High Isle Antiquities (5 leads from High Isle & Amenos)", 1, [
        (1, "Gain Major Berserk, Major Courage, Major Force, Major Heroism, Major Protection, Major Prophecy, Major Resolve, Major Savagery, Major Sorcery, and Minor Fortitude at all times. Reduces your Ultimate generation by 50%."),
    ]),
    ("Harpooner's Wading Kilt", "Mythic", "Galen & Y'ffelon Antiquities (5 leads)", 1, [
        (1, "When you deal a Critical Strike, you gain a stack of Hunter's Focus for 10 seconds, up to 5 stacks. Each stack increases your Weapon and Spell Critical by 220 and Critical Damage by 2%. At 5 stacks, you gain an additional 10% Critical Damage and your stacks no longer expire."),
    ]),
    ("Ring of the Pale Order", "Mythic", "Western Skyrim Antiquities (5 leads)", 1, [
        (1, "You cannot gain healing or Damage Shields from other players. Increases your self-healing done by 25% for each player in your group, up to a maximum of 100%."),
    ]),
    ("Malacath's Band of Brutality", "Mythic", "Deadlands & Fargrave Antiquities (5 leads)", 1, [
        (1, "Your Critical Strikes deal no additional damage. You gain 18% bonus damage for each 1000 Weapon and Spell Critical rating you have."),
    ]),
    ("Gaze of Sithis", "Mythic", "Western Skyrim & Blackreach Antiquities (5 leads)", 1, [
        (1, "Adds 16000 Max Health, 5948 Physical Resistance and Spell Resistance. Makes you immune to Execution effects. Reduces your Magicka and Stamina Recovery by 50%."),
    ]),
    ("Bloodlord's Embrace", "Mythic", "Reaper's March & Bangkorai Antiquities (5 leads)", 1, [
        (1, "Dealing damage with a Bash attack grants you a persistent stack of Bloodlord's Pact. Each stack increases your Spell and Physical Resistance by 600 and causes nearby enemies to bleed at 20 stacks."),
    ]),
    ("Snow Treaders", "Mythic", "Western Skyrim Antiquities (5 leads)", 1, [
        (1, "You are immune to the effects of Snares and Immobilizations that are less than 100% Movement Speed reduction, but your Movement Speed cannot be increased above the base cap."),
    ]),
    ("Thrassian Stranglers", "Mythic", "Summerset Antiquities (5 leads)", 1, [
        (1, "Killing an enemy grants you a permanent stack of Slaughter. Each stack increases your Spell and Weapon Damage by 5 but reduces your Max Health by 100. Max 50 stacks."),
    ]),
    ("Torc of Tonal Constancy", "Mythic", "Blackwood Antiquities (5 leads)", 1, [
        (1, "When your Stamina is higher than your Magicka, gain Minor Resolve. When Magicka is higher than Stamina, gain Minor Fortitude. When equal, gain both."),
    ]),
    ("Death Dealer's Fete", "Mythic", "Deadlands Antiquities (5 leads)", 1, [
        (1, "Dealing damage has a 20% chance to increase your highest stat (Health, Magicka, or Stamina) by 450 for 20 seconds, stacking up to 5 times. Each type of stat can only have one stack at a time."),
    ]),
    ("Spaulder of Ruin", "Mythic", "Blackwood Antiquities (5 leads)", 1, [
        (1, "When you take damage from a nearby enemy, you deal Physical Damage to them. This effect can occur once every 3 seconds and stacks up to 6 times. The Spaulder gains power the more damage you take."),
    ]),
    ("Markyn Ring of Majesty", "Mythic", "Necrom Antiquities (5 leads)", 1, [
        (1, "When you activate an Ultimate ability, you and up to 5 nearby group members gain Major Courage and Major Berserk for 8 seconds."),
    ]),
    ("Velothi Ur-Mage's Amulet", "Mythic", "Necrom Antiquities (5 leads)", 1, [
        (1, "When you deal damage, you have a 15% chance to deal bonus Magic Damage in an area and grant yourself Minor Aegis, reducing damage from Dungeon, Trial, and Arena monsters by 5% for 20 seconds. The bonus damage increases by 1% each time this triggers, up to 50%."),
    ]),
    ("Shapeshifter's Chain", "Mythic", "Gold Road Antiquities (5 leads)", 1, [
        (1, "Transforming into a Vampire, Werewolf, or Arcanist's Soldier of Apocrypha form grants you up to 1528 Weapon and Spell Damage based on the transformation's cooldown."),
    ]),

    # ══════════════════════════════════════════════════════════════════════════
    # PVP  (drop from Cyrodiil vendors, Imperial City, and Battlegrounds)
    # ══════════════════════════════════════════════════════════════════════════

    ("Eternal Vigor", "PvP", "Cyrodiil Elite Gear Vendor", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 1206 Health Recovery"),
        (4, "Adds 1096 Max Health"),
        (5, "Adds 1206 Stamina Recovery and 1206 Magicka Recovery"),
    ]),
    ("Cyrodiil's Light", "PvP", "Cyrodiil Elite Gear Vendor", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Magicka"),
        (5, "When you deal a Critical Strike, you generate 10 Ultimate. This effect can occur once every 4 seconds."),
    ]),
    ("Force of Nature", "PvP", "Cyrodiil Elite Gear Vendor", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you take damage that reduces you below 40% Health, you gain a Damage Shield for 6 seconds. This effect can occur once every 30 seconds."),
    ]),
    ("Wrath of Elements", "PvP", "Cyrodiil Elite Gear Vendor", 5, [
        (2, "Adds 1096 Max Magicka"),
        (3, "Adds 129 Weapon and Spell Damage"),
        (4, "Adds 1096 Max Magicka"),
        (5, "Increases your damage with Fire, Frost, and Shock abilities by 10%."),
    ]),
    ("Reactive Armor", "PvP", "Imperial City (Tel Var Stones vendor)", 5, [
        (2, "Adds 1096 Max Health"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Health"),
        (5, "When you take damage, you have a 10% chance to gain 5948 Physical Resistance and Spell Resistance for 5 seconds. This effect can occur once every 5 seconds."),
    ]),
    ("Soldier of Anguish", "PvP", "Imperial City (Tel Var Stones vendor)", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 4936 Physical Resistance"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal melee damage, you have a 15% chance to immobilize the enemy for 2 seconds. This effect can occur once every 5 seconds."),
    ]),
    ("Ravager", "PvP", "Cyrodiil Elite Gear Vendor", 5, [
        (2, "Adds 1096 Max Stamina"),
        (3, "Adds 657 Weapon and Spell Critical"),
        (4, "Adds 1096 Max Stamina"),
        (5, "When you deal damage with a melee ability, you apply Ravage to the enemy for 15 seconds, reducing their Healing Received by 10% and dealing Physical Damage over time. This effect can occur once every 15 seconds."),
    ]),
]

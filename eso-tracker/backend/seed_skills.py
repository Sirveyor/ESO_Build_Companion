"""
ESO active skill seed data — base skill names and their two morph options.
Passives are excluded (they don't go on the skill bar).
Format: (id, skill_line_id, name, morph_1, morph_2, is_ultimate)
"""

SKILLS = [

    # ══════════════════════════════════════════════════════════════════════════
    # DRAGONKNIGHT
    # ══════════════════════════════════════════════════════════════════════════

    # Ardent Flame
    ("sk-dk-ard-1", "sl-dk-ardent", "Lava Whip",             "Flame Lash",             "Power Lash",                0),
    ("sk-dk-ard-2", "sl-dk-ardent", "Searing Strike",         "Burning Embers",         "Venomous Claw",             0),
    ("sk-dk-ard-3", "sl-dk-ardent", "Fiery Breath",           "Noxious Breath",         "Engulfing Flames",          0),
    ("sk-dk-ard-4", "sl-dk-ardent", "Fiery Grip",             "Extended Chains",        "Unrelenting Grip",          0),
    ("sk-dk-ard-5", "sl-dk-ardent", "Inferno",                "Cauterize",              "Flames of Oblivion",        0),
    ("sk-dk-ard-u", "sl-dk-ardent", "Dragonknight Standard",  "Shifting Standard",      "Standard of Might",         1),

    # Draconic Power
    ("sk-dk-dra-1", "sl-dk-draconic", "Spiked Armor",         "Volatile Armor",         "Hardened Armor",            0),
    ("sk-dk-dra-2", "sl-dk-draconic", "Dark Talons",          "Choking Talons",         "Burning Talons",            0),
    ("sk-dk-dra-3", "sl-dk-draconic", "Dragon Blood",         "Coagulating Blood",      "Green Dragon Blood",        0),
    ("sk-dk-dra-4", "sl-dk-draconic", "Reflective Scale",     "Reflective Plate",       "Dragon Fire Scale",         0),
    ("sk-dk-dra-5", "sl-dk-draconic", "Inhale",               "Draw Essence",           "Deep Breath",               0),
    ("sk-dk-dra-u", "sl-dk-draconic", "Dragon Leap",          "Ferocious Leap",         "Take Flight",               1),

    # Earthen Heart
    ("sk-dk-ear-1", "sl-dk-earthen", "Stonefist",             "Stone Giant",            "Obsidian Shard",            0),
    ("sk-dk-ear-2", "sl-dk-earthen", "Molten Weapons",        "Igneous Weapons",        "Molten Armaments",          0),
    ("sk-dk-ear-3", "sl-dk-earthen", "Ash Cloud",             "Cinder Storm",           "Eruption",                  0),
    ("sk-dk-ear-4", "sl-dk-earthen", "Obsidian Shield",       "Igneous Shield",         "Fragmented Shield",         0),
    ("sk-dk-ear-5", "sl-dk-earthen", "Petrify",               "Fossilize",              "Shattering Rocks",          0),
    ("sk-dk-ear-u", "sl-dk-earthen", "Magma Armor",           "Magma Shell",            "Corrosive Armor",           1),

    # ══════════════════════════════════════════════════════════════════════════
    # SORCERER
    # ══════════════════════════════════════════════════════════════════════════

    # Daedric Summoning
    ("sk-so-dae-1", "sl-sorc-daedric", "Summon Unstable Familiar", "Summon Volatile Familiar",  "Summon Unstable Clannfear", 0),
    ("sk-so-dae-2", "sl-sorc-daedric", "Conjured Ward",            "Empowered Ward",             "Annulment",                 0),
    ("sk-so-dae-3", "sl-sorc-daedric", "Bound Armor",              "Bound Armaments",            "Bound Aegis",               0),
    ("sk-so-dae-4", "sl-sorc-daedric", "Summon Winged Twilight",   "Summon Twilight Matriarch",  "Summon Twilight Tormentor", 0),
    ("sk-so-dae-5", "sl-sorc-daedric", "Daedric Mines",            "Daedric Mines",              "Daedric Tomb",              0),
    ("sk-so-dae-u", "sl-sorc-daedric", "Summon Storm Atronach",    "Greater Storm Atronach",     "Summon Charged Atronach",   1),

    # Dark Magic
    ("sk-so-dar-1", "sl-sorc-dark", "Crystal Shard",   "Crystal Fragments",  "Crystal Weapon",        0),
    ("sk-so-dar-2", "sl-sorc-dark", "Encase",           "Restraining Prison", "Shattering Prison",     0),
    ("sk-so-dar-3", "sl-sorc-dark", "Rune Prison",      "Rune Cage",          "Defensive Rune",        0),
    ("sk-so-dar-4", "sl-sorc-dark", "Dark Exchange",    "Dark Deal",          "Dark Conversion",       0),
    ("sk-so-dar-u", "sl-sorc-dark", "Negate Magic",     "Suppression Field",  "Absorption Field",      1),

    # Storm Calling
    ("sk-so-sto-1", "sl-sorc-storm", "Mages' Fury",     "Endless Fury",       "Mages' Wrath",          0),
    ("sk-so-sto-2", "sl-sorc-storm", "Lightning Form",  "Hurricane",          "Boundless Storm",       0),
    ("sk-so-sto-3", "sl-sorc-storm", "Bolt Escape",     "Ball of Lightning",  "Streak",                0),
    ("sk-so-sto-4", "sl-sorc-storm", "Lightning Surge", "Power Surge",        "Critical Surge",        0),
    ("sk-so-sto-5", "sl-sorc-storm", "Summon Storm Servant", "Summon Charged Atronach", "Greater Storm Atronach", 0),
    ("sk-so-sto-u", "sl-sorc-storm", "Overload",        "Energy Overload",    "Power Overload",        1),

    # ══════════════════════════════════════════════════════════════════════════
    # NIGHTBLADE
    # ══════════════════════════════════════════════════════════════════════════

    # Assassination
    ("sk-nb-ass-1", "sl-nb-assassin", "Assassin's Blade",  "Killer's Blade",   "Impale",                0),
    ("sk-nb-ass-2", "sl-nb-assassin", "Teleport Strike",   "Ambush",           "Lotus Fan",             0),
    ("sk-nb-ass-3", "sl-nb-assassin", "Blur",              "Phantasmal Escape","Mirage",                0),
    ("sk-nb-ass-4", "sl-nb-assassin", "Mark Target",       "Piercing Mark",    "Reaper's Mark",         0),
    ("sk-nb-ass-5", "sl-nb-assassin", "Grim Focus",        "Merciless Resolve","Relentless Focus",      0),
    ("sk-nb-ass-u", "sl-nb-assassin", "Death Stroke",      "Incapacitating Strike", "Soul Harvest",     1),

    # Shadow
    ("sk-nb-sha-1", "sl-nb-shadow", "Shadow Cloak",       "Dark Cloak",        "Shadowy Disguise",      0),
    ("sk-nb-sha-2", "sl-nb-shadow", "Veiled Strike",      "Surprise Attack",   "Concealed Weapon",      0),
    ("sk-nb-sha-3", "sl-nb-shadow", "Path of Darkness",   "Refreshing Path",   "Twisting Path",         0),
    ("sk-nb-sha-4", "sl-nb-shadow", "Aspect of Terror",   "Mass Hysteria",     "Manifestation of Terror",0),
    ("sk-nb-sha-5", "sl-nb-shadow", "Summon Shade",       "Dark Shade",        "Shadow Image",          0),
    ("sk-nb-sha-u", "sl-nb-shadow", "Consuming Darkness", "Bolstering Darkness","Veil of Blades",       1),

    # Siphoning
    ("sk-nb-sip-1", "sl-nb-siphon", "Strife",             "Funnel Health",     "Swallow Soul",          0),
    ("sk-nb-sip-2", "sl-nb-siphon", "Agony",              "Prolonged Suffering","Malefic Wreath",       0),
    ("sk-nb-sip-3", "sl-nb-siphon", "Cripple",            "Debilitate",        "Crippling Grasp",       0),
    ("sk-nb-sip-4", "sl-nb-siphon", "Siphoning Attacks",  "Siphoning Strikes", "Leeching Strikes",      0),
    ("sk-nb-sip-5", "sl-nb-siphon", "Drain Power",        "Power Extraction",  "Sap Essence",           0),
    ("sk-nb-sip-u", "sl-nb-siphon", "Soul Shred",         "Soul Siphon",       "Soul Tether",           1),

    # ══════════════════════════════════════════════════════════════════════════
    # TEMPLAR
    # ══════════════════════════════════════════════════════════════════════════

    # Aedric Spear
    ("sk-tp-aed-1", "sl-tp-aedric", "Puncturing Strikes",  "Biting Jabs",       "Puncturing Sweep",      0),
    ("sk-tp-aed-2", "sl-tp-aedric", "Spear Shards",        "Luminous Shards",   "Blazing Spear",         0),
    ("sk-tp-aed-3", "sl-tp-aedric", "Sun Shield",          "Radiant Ward",      "Blazing Shield",        0),
    ("sk-tp-aed-4", "sl-tp-aedric", "Focused Charge",      "Toppling Charge",   "Aurora Javelin",        0),
    ("sk-tp-aed-5", "sl-tp-aedric", "Piercing Javelin",    "Binding Javelin",   "Explosive Charge",      0),
    ("sk-tp-aed-u", "sl-tp-aedric", "Radial Sweep",        "Empowering Sweep",  "Crescent Sweep",        1),

    # Dawn's Wrath
    ("sk-tp-daw-1", "sl-tp-dawns", "Solar Flare",          "Dark Flare",        "Solar Barrage",         0),
    ("sk-tp-daw-2", "sl-tp-dawns", "Sun Fire",             "Reflective Light",  "Unstable Core",         0),
    ("sk-tp-daw-3", "sl-tp-dawns", "Backlash",             "Power of the Light","Purifying Light",       0),
    ("sk-tp-daw-4", "sl-tp-dawns", "Radiant Destruction",  "Radiant Oppressor", "Radiant Glory",         0),
    ("sk-tp-daw-u", "sl-tp-dawns", "Nova",                 "Solar Prison",      "Solar Disturbance",     1),

    # Restoring Light
    ("sk-tp-res-1", "sl-tp-restoring", "Rushed Ceremony",  "Breath of Life",    "Honor the Dead",        0),
    ("sk-tp-res-2", "sl-tp-restoring", "Healing Ritual",   "Ritual of Rebirth", "Hasty Prayer",          0),
    ("sk-tp-res-3", "sl-tp-restoring", "Restoring Aura",   "Repentance",        "Radiant Aura",          0),
    ("sk-tp-res-4", "sl-tp-restoring", "Cleansing Ritual", "Extended Ritual",   "Purifying Ritual",      0),
    ("sk-tp-res-u", "sl-tp-restoring", "Rite of Passage",  "Remembrance",       "Practiced Incantation", 1),

    # ══════════════════════════════════════════════════════════════════════════
    # WARDEN
    # ══════════════════════════════════════════════════════════════════════════

    # Animal Companions
    ("sk-wd-ani-1", "sl-wd-animal", "Dive",               "Cutting Dive",       "Screaming Cliff Racer", 0),
    ("sk-wd-ani-2", "sl-wd-animal", "Swarm",              "Growing Swarm",      "Fetcher Infection",     0),
    ("sk-wd-ani-3", "sl-wd-animal", "Betty Netch",        "Blue Betty",         "Bull Netch",            0),
    ("sk-wd-ani-4", "sl-wd-animal", "Scorch",             "Subterranean Assault","Deep Fissure",         0),
    ("sk-wd-ani-5", "sl-wd-animal", "Falcon's Ferocity",  "Bird of Prey",       "Deceptive Predator",    0),
    ("sk-wd-ani-u", "sl-wd-animal", "Feral Guardian",     "Eternal Guardian",   "Wild Guardian",         1),

    # Green Balance
    ("sk-wd-gre-1", "sl-wd-green", "Fungal Growth",       "Enchanted Growth",   "Soothing Spores",       0),
    ("sk-wd-gre-2", "sl-wd-green", "Lotus Flower",        "Lotus Blossom",      "Green Lotus",           0),
    ("sk-wd-gre-3", "sl-wd-green", "Living Trellis",      "Leeching Vines",     "Corrupted Pollen",      0),
    ("sk-wd-gre-4", "sl-wd-green", "Healing Seed",        "Budding Seeds",      "Corrupted Seed Pod",    0),
    ("sk-wd-gre-5", "sl-wd-green", "Vigor",               "Echoing Vigor",      "Resolving Vigor",       0),
    ("sk-wd-gre-u", "sl-wd-green", "Secluded Grove",      "Enchanted Forest",   "Nature's Embrace",      1),

    # Winter's Embrace
    ("sk-wd-win-1", "sl-wd-winter", "Frost Cloak",        "Expansive Frost Cloak","Ice Fortress",        0),
    ("sk-wd-win-2", "sl-wd-winter", "Crystallized Shield","Crystallized Slab",  "Shimmering Shield",     0),
    ("sk-wd-win-3", "sl-wd-winter", "Arctic Blast",       "Arctic Wind",        "Icy Aura",              0),
    ("sk-wd-win-4", "sl-wd-winter", "Impaling Shards",    "Winter's Revenge",   "Gripping Shards",       0),
    ("sk-wd-win-5", "sl-wd-winter", "Frozen Gate",        "Frozen Device",      "Frozen Retreat",        0),
    ("sk-wd-win-u", "sl-wd-winter", "Sleet Storm",        "Permafrost",         "Northern Storm",        1),

    # ══════════════════════════════════════════════════════════════════════════
    # NECROMANCER
    # ══════════════════════════════════════════════════════════════════════════

    # Grave Lord
    ("sk-nc-gra-1", "sl-nc-grave", "Flame Skull",         "Venom Skull",        "Ricochet Skull",        0),
    ("sk-nc-gra-2", "sl-nc-grave", "Boneyard",            "Unnerving Boneyard", "Avid Boneyard",         0),
    ("sk-nc-gra-3", "sl-nc-grave", "Skeletal Mage",       "Skeletal Archer",    "Skeletal Arcanist",     0),
    ("sk-nc-gra-4", "sl-nc-grave", "Shocking Siphon",     "Detonating Siphon",  "Mystic Siphon",         0),
    ("sk-nc-gra-5", "sl-nc-grave", "Blastbones",          "Stalking Blastbones","Blighted Blastbones",   0),
    ("sk-nc-gra-u", "sl-nc-grave", "Frozen Colossus",     "Glacial Colossus",   "Pestilent Colossus",    1),

    # Bone Tyrant
    ("sk-nc-bon-1", "sl-nc-bone", "Death Scythe",         "Ruinous Scythe",     "Hungry Scythe",         0),
    ("sk-nc-bon-2", "sl-nc-bone", "Bone Totem",           "Remote Totem",       "Agony Totem",           0),
    ("sk-nc-bon-3", "sl-nc-bone", "Bitter Harvest",       "Deaden Pain",        "Necrotic Potency",      0),
    ("sk-nc-bon-4", "sl-nc-bone", "Grave Grasp",          "Ghostly Embrace",    "Empowering Grasp",      0),
    ("sk-nc-bon-5", "sl-nc-bone", "Bone Wall",            "Beckoning Armor",    "Summoner's Armor",      0),
    ("sk-nc-bon-u", "sl-nc-bone", "Goliath Transformation","Ravenous Goliath",  "Pummeling Goliath",     1),

    # Living Death
    ("sk-nc-liv-1", "sl-nc-living", "Render Flesh",       "Blood Sacrifice",    "Resistant Flesh",       0),
    ("sk-nc-liv-2", "sl-nc-living", "Expunge",            "Expunge and Modify", "Hexproof",              0),
    ("sk-nc-liv-3", "sl-nc-living", "Renewing Animation", "Restoring Tether",   "Animate Blastbones",    0),
    ("sk-nc-liv-4", "sl-nc-living", "Spirit Guardian",    "Spirit Mender",      "Intensive Mender",      0),
    ("sk-nc-liv-5", "sl-nc-living", "Braided Tether",     "Life Amid Death",    "Restoring Aura",        0),
    ("sk-nc-liv-u", "sl-nc-living", "Life amid Death",    "Reanimate",          "Renewing Animation",    1),

    # ══════════════════════════════════════════════════════════════════════════
    # ARCANIST  (Necrom, 2023)
    # ══════════════════════════════════════════════════════════════════════════

    # Herald of the Tome
    ("sk-arc-her-1", "sl-arc-herald", "Runeblades",          "Cephaliarch's Flail",     "Pragmatic Fatecarver",    0),
    ("sk-arc-her-2", "sl-arc-herald", "Abyssal Impact",      "Tentacular Dread",        "Sea of Consciousness",    0),
    ("sk-arc-her-3", "sl-arc-herald", "Fulminating Rune",    "Thunder Burst",           "Cascading Fortune",       0),
    ("sk-arc-her-4", "sl-arc-herald", "Writhing Runeform",   "Rune of Displacement",    "Rune of Eldritch Horror", 0),
    ("sk-arc-her-u", "sl-arc-herald", "The Imperfect Ring",  "Fatewoven Net",           "Runeblades Codex",        1),

    # Soldier of Apocrypha
    ("sk-arc-sol-1", "sl-arc-soldier", "Chakram of Destiny", "Inexorable Presence",     "Inevitable Ally",         0),
    ("sk-arc-sol-2", "sl-arc-soldier", "Wield Soul",         "Runeguard of Still Waters","Runeguard of Freedom",   0),
    ("sk-arc-sol-3", "sl-arc-soldier", "Hardened Ward",      "Spined Carapace",         "Runic Jabs",              0),
    ("sk-arc-sol-4", "sl-arc-soldier", "Cephaliarch's Flail","Tome-Bearer's Inspiration","Apocryphal Soldier",     0),
    ("sk-arc-sol-u", "sl-arc-soldier", "Fate Unraveler",     "Rune Prison",             "The Tide King's Gaze",    1),

    # Curative Runeforms
    ("sk-arc-cur-1", "sl-arc-curative", "Remedy Cascade",    "Evolving Runemend",       "Runemend",                0),
    ("sk-arc-cur-2", "sl-arc-curative", "Apocryphal Gate",   "Rune of Displacement",    "Rune of the Colorless Pool",0),
    ("sk-arc-cur-3", "sl-arc-curative", "Inspired Scholarship","Recuperative Treatise", "Crux of the Manuscript",  0),
    ("sk-arc-cur-u", "sl-arc-curative", "Curative Runeforms","Curative Rune",           "Intensive Mender",        1),

    # ══════════════════════════════════════════════════════════════════════════
    # WEAPON SKILLS
    # ══════════════════════════════════════════════════════════════════════════

    # Two Handed
    ("sk-wep-2h-1", "sl-wep-2h", "Uppercut",              "Dizzying Swing",     "Wrecking Blow",         0),
    ("sk-wep-2h-2", "sl-wep-2h", "Carve",                 "Brawler",            "Cleave",                0),
    ("sk-wep-2h-3", "sl-wep-2h", "Reverse Slash",         "Reverse Slice",      "Executioner",           0),
    ("sk-wep-2h-4", "sl-wep-2h", "Critical Charge",       "Stampede",           "Critical Rush",         0),
    ("sk-wep-2h-5", "sl-wep-2h", "Momentum",              "Forward Momentum",   "Rally",                 0),
    ("sk-wep-2h-u", "sl-wep-2h", "Berserker Strike",      "Berserker Rage",     "Onslaught",             1),

    # One Hand and Shield
    ("sk-wep-1s-1", "sl-wep-1s", "Puncture",              "Pierce Armor",       "Ransack",               0),
    ("sk-wep-1s-2", "sl-wep-1s", "Low Slash",             "Heroic Slash",       "Deep Slash",            0),
    ("sk-wep-1s-3", "sl-wep-1s", "Shield Assault",        "Invasion",           "Power Bash",            0),
    ("sk-wep-1s-4", "sl-wep-1s", "Defensive Posture",     "Defensive Stance",   "Absorb Missile",        0),
    ("sk-wep-1s-5", "sl-wep-1s", "Shielded Assault",      "Shield Assault",     "Reverberating Bash",    0),
    ("sk-wep-1s-u", "sl-wep-1s", "Shield Wall",           "Spell Wall",         "Fortress",              1),

    # Dual Wield
    ("sk-wep-dw-1", "sl-wep-dw", "Twin Slashes",          "Rending Slashes",    "Blood Craze",           0),
    ("sk-wep-dw-2", "sl-wep-dw", "Flurry",                "Rapid Strikes",      "Bloodthirst",           0),
    ("sk-wep-dw-3", "sl-wep-dw", "Hidden Blade",          "Flying Blade",       "Shrouded Daggers",      0),
    ("sk-wep-dw-4", "sl-wep-dw", "Blade Cloak",           "Deadly Cloak",       "Quick Cloak",           0),
    ("sk-wep-dw-5", "sl-wep-dw", "Whirlwind",             "Steel Tornado",      "Whirling Blades",       0),
    ("sk-wep-dw-u", "sl-wep-dw", "Lacerate",              "Rend",               "Hemorrhage",            1),

    # Bow
    ("sk-wep-bow-1", "sl-wep-bow", "Snipe",               "Lethal Arrow",       "Focused Aim",           0),
    ("sk-wep-bow-2", "sl-wep-bow", "Volley",              "Arrow Barrage",      "Endless Hail",          0),
    ("sk-wep-bow-3", "sl-wep-bow", "Scatter Shot",        "Magnum Shot",        "Draining Shot",         0),
    ("sk-wep-bow-4", "sl-wep-bow", "Poison Arrow",        "Poison Injection",   "Venom Arrow",           0),
    ("sk-wep-bow-5", "sl-wep-bow", "Arrow Spray",         "Bombard",            "Acid Spray",            0),
    ("sk-wep-bow-u", "sl-wep-bow", "Ballista",            "Scorched Earth",     "Toxic Barrage",         1),

    # Destruction Staff
    ("sk-wep-ds-1", "sl-wep-destro", "Force Shock",        "Crushing Shock",    "Force Pulse",           0),
    ("sk-wep-ds-2", "sl-wep-destro", "Wall of Elements",   "Unstable Wall of Elements","Elemental Blockade",0),
    ("sk-wep-ds-3", "sl-wep-destro", "Impulse",            "Elemental Ring",    "Pulsar",                0),
    ("sk-wep-ds-4", "sl-wep-destro", "Destructive Touch",  "Destructive Clench","Destructive Reach",     0),
    ("sk-wep-ds-5", "sl-wep-destro", "Weakness to Elements","Elemental Drain",  "Elemental Susceptibility",0),
    ("sk-wep-ds-u", "sl-wep-destro", "Elemental Storm",    "Elemental Rage",    "Eye of the Storm",      1),

    # Restoration Staff
    ("sk-wep-rs-1", "sl-wep-resto", "Grand Healing",       "Illustrious Healing","Healing Springs",      0),
    ("sk-wep-rs-2", "sl-wep-resto", "Regeneration",        "Mutagen",            "Rapid Regeneration",   0),
    ("sk-wep-rs-3", "sl-wep-resto", "Healing Ward",        "Steadfast Ward",     "Restoration Ward",     0),
    ("sk-wep-rs-4", "sl-wep-resto", "Blessing of Protection","Combat Prayer",    "Blessing of Restoration",0),
    ("sk-wep-rs-5", "sl-wep-resto", "Force Siphon",        "Siphon Spirit",      "Drain Power",          0),
    ("sk-wep-rs-u", "sl-wep-resto", "Panacea",             "Life Giver",         "Replenishing Barrier", 1),

    # ══════════════════════════════════════════════════════════════════════════
    # GUILD SKILLS
    # ══════════════════════════════════════════════════════════════════════════

    # Fighters Guild
    ("sk-gu-fg-1", "sl-guild-fighters", "Silver Bolts",       "Silver Leash",      "Silver Shards",         0),
    ("sk-gu-fg-2", "sl-guild-fighters", "Trap Beast",         "Barbed Trap",       "Lightweight Beast Trap",0),
    ("sk-gu-fg-3", "sl-guild-fighters", "Camouflaged Hunter", "Expert Hunter",     "Evil Hunter",           0),
    ("sk-gu-fg-4", "sl-guild-fighters", "Circle of Protection","Turn Undead",      "Ring of Preservation",  0),
    ("sk-gu-fg-u", "sl-guild-fighters", "Dawnbreaker",        "Flawless Dawnbreaker","Dawnbreaker of Smiting",1),

    # Mages Guild
    ("sk-gu-mg-1", "sl-guild-mages", "Magelight",            "Inner Light",        "Radiant Magelight",     0),
    ("sk-gu-mg-2", "sl-guild-mages", "Entropy",              "Degeneration",       "Structured Entropy",    0),
    ("sk-gu-mg-3", "sl-guild-mages", "Fire Rune",            "Volcanic Rune",      "Scalding Rune",         0),
    ("sk-gu-mg-4", "sl-guild-mages", "Equilibrium",          "Spell Symmetry",     "Balance",               0),
    ("sk-gu-mg-u", "sl-guild-mages", "Meteor",               "Ice Comet",          "Shooting Star",         1),

    # Undaunted
    ("sk-gu-un-1", "sl-guild-undaunted", "Necrotic Orb",     "Mystic Orb",         "Energy Orb",            0),
    ("sk-gu-un-2", "sl-guild-undaunted", "Inner Fire",       "Inner Rage",         "Inner Beast",           0),
    ("sk-gu-un-3", "sl-guild-undaunted", "Bone Shield",      "Spiked Bone Shield", "Bone Surge",            0),
    ("sk-gu-un-4", "sl-guild-undaunted", "Trapping Webs",    "Shadow Silk",        "Tangling Webs",         0),
    ("sk-gu-un-5", "sl-guild-undaunted", "Blood Altar",      "Overflowing Altar",  "Sanguine Altar",        0),

    # Thieves Guild
    ("sk-gu-tg-1", "sl-guild-thieves", "Finders Keepers",    "Swipe",              "Burst of Speed",        0),
    ("sk-gu-tg-2", "sl-guild-thieves", "Slip Away",          "Elusive Mist",       "Fade",                  0),
    ("sk-gu-tg-3", "sl-guild-thieves", "Larceny",            "Haggling",           "Clemency",              0),

    # Dark Brotherhood
    ("sk-gu-db-1", "sl-guild-db", "Blade of Woe",            None,                 None,                    0),
    ("sk-gu-db-2", "sl-guild-db", "Shadowy Supplier",        None,                 None,                    0),

    # Psijic Order
    ("sk-gu-ps-1", "sl-guild-psijic", "Time Stop",            "Borrowed Time",     "Time Freeze",           0),
    ("sk-gu-ps-2", "sl-guild-psijic", "Imbue Weapon",         "Elemental Weapon",  "Crushing Weapon",       0),
    ("sk-gu-ps-3", "sl-guild-psijic", "Accelerate",           "Surge",             "Channeled Acceleration", 0),
    ("sk-gu-ps-4", "sl-guild-psijic", "Meditate",             "Deep Thoughts",     "Contemplation",         0),
    ("sk-gu-ps-5", "sl-guild-psijic", "Undo",                 "Precognition",      "Temporal Guard",        0),
    ("sk-gu-ps-u", "sl-guild-psijic", "Nova",                 "Spatial Awareness", "Unbound Chaos",         1),

    # ══════════════════════════════════════════════════════════════════════════
    # ALLIANCE WAR
    # ══════════════════════════════════════════════════════════════════════════

    # Assault
    ("sk-aw-as-1", "sl-aw-assault", "Rapid Maneuver",        "Charging Maneuver",  "Retreating Maneuver",   0),
    ("sk-aw-as-2", "sl-aw-assault", "Caltrops",              "Anti-Cavalry Caltrops","Razor Caltrops",       0),
    ("sk-aw-as-3", "sl-aw-assault", "Vigor",                 "Echoing Vigor",      "Resolving Vigor",       0),
    ("sk-aw-as-4", "sl-aw-assault", "Magicka Detonation",    "Inevitable Detonation","Proximity Detonation", 0),
    ("sk-aw-as-u", "sl-aw-assault", "War Horn",              "Aggressive Warhorn", "Sturdy Horn",           1),

    # Support
    ("sk-aw-su-1", "sl-aw-support", "Guard",                 "Mystic Guard",       "Stalwart Guard",        0),
    ("sk-aw-su-2", "sl-aw-support", "Barrier",               "Reviving Barrier",   "Replenishing Barrier",  0),
    ("sk-aw-su-3", "sl-aw-support", "Siege Shield",          "Siege Weapon Shield","Propelling Shield",     0),
    ("sk-aw-su-4", "sl-aw-support", "Purge",                 "Efficient Purge",    "Cleanse",               0),
    ("sk-aw-su-u", "sl-aw-support", "Phalanx",               "Defensive Formation","Sturdy Defense",        1),

    # ══════════════════════════════════════════════════════════════════════════
    # WORLD SKILLS
    # ══════════════════════════════════════════════════════════════════════════

    # Soul Magic
    ("sk-wo-so-1", "sl-world-soul", "Soul Trap",             "Soul Splitting Trap","Consuming Trap",        0),
    ("sk-wo-so-2", "sl-world-soul", "Soul Strike",           "Soul Assault",       "Shatter Soul",          0),
    ("sk-wo-so-u", "sl-world-soul", "Soul Strike",           "Soul Assault",       "Shatter Soul",          1),

    # Vampire
    ("sk-wo-va-1", "sl-world-vampire", "Drain",              "Simmering Frenzy",   "Exhilarating Drain",    0),
    ("sk-wo-va-2", "sl-world-vampire", "Mist Form",          "Elusive Mist",       "Healthy Return",        0),
    ("sk-wo-va-3", "sl-world-vampire", "Mesmerize",          "Hypnosis",           "Stupefy",               0),
    ("sk-wo-va-4", "sl-world-vampire", "Blood Scion",        "Perfect Blood Scion","Swarming Scion",        0),
    ("sk-wo-va-u", "sl-world-vampire", "Vampire's Bane",     "Blood Scion",        "Perfect Blood Scion",   1),

    # Werewolf
    ("sk-wo-ww-1", "sl-world-werewolf", "Pounce",            "Brutal Pounce",      "Feral Pounce",          0),
    ("sk-wo-ww-2", "sl-world-werewolf", "Roar",              "Ferocious Roar",     "Deafening Roar",        0),
    ("sk-wo-ww-3", "sl-world-werewolf", "Hircine's Rage",    "Pack Leader",        "Werewolf Berserker",    0),
    ("sk-wo-ww-4", "sl-world-werewolf", "Infectious Claws",  "Claws of Anguish",   "Claws of Life",         0),
    ("sk-wo-ww-u", "sl-world-werewolf", "Werewolf Transformation","Pack Leader",    "Werewolf Berserker",   1),

    # Legerdemain
    ("sk-wo-le-1", "sl-world-legerdemain", "Pickpocket",      None,                 None,                   0),
    ("sk-wo-le-2", "sl-world-legerdemain", "Lockpicking",     None,                 None,                   0),
]

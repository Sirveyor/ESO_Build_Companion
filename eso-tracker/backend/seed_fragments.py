"""
ESO Fragments collectible seed data, pulled from UESP's Online:Fragments page.
Format: (set_name, category, [(item_name, source), ...])
  category = Public Dungeon | Event | Prologue Quest | Tales of Tribute
             | Infinite Archive | Skill Style
  source   = short factual location/method note for that piece; None when
             the wiki itself has no source listed (marked "Pages Missing Data")

Three additional collections (Soulfire Dragon Illusion, Unstable Morpholith,
Nascent Indrik) live on their own separate UESP pages and aren't included here.
"""

FRAGMENT_SETS = [
    # --- Public Dungeon ---
    ('Dwarven Theodolite', 'Public Dungeon', [
            ('Dwarven Theodolite Wheels', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Torso', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Shoulder', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Neck', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Head', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Eye', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
            ('Dwarven Theodolite Chassis', 'Find and reassemble its seven parts in Nchuleftingth in Vvardenfell'),
        ]),
    ('Sixth House Robe', 'Public Dungeon', [
            ('Sixth House Incense of Toolwork', 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ('Sixth House Ornamental Fasteners', 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ('Sixth House Patterned Bolt', 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ("Sixth House Tailor's Bell", 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ("Sixth House Tailor's Hammer", 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ("Sixth House Tailor's Shears", 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
            ('Sixth House Writhing Thread', 'Collect seven parts in the Forgotten Wastes in Vvardenfell'),
        ]),
    ('Big-Eared Ginger Kitten', 'Public Dungeon', [
            ("Big-Eared Ginger Kitten's Collar", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ("Big-Eared Ginger Kitten's Tag", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ("Big-Eared Ginger Kitten's Milk Saucer", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ("Big-Eared Ginger Kitten's Bait Mouse", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ("Big-Eared Ginger Kitten's Sleeping-Basket", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ("Big-Eared Ginger Kitten's Feather Toy", 'Collect seven runebox fragments in Karnwasten in Summerset'),
            ('Big-Eared Ginger Kitten\'s "Care and Feeding" Guide', 'Collect seven runebox fragments in Karnwasten in Summerset'),
        ]),
    ('Psijic Glowglobe', 'Public Dungeon', [
            ("Psijic Glowglobe's Ancient Texts", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Conjectural Writings", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Updated Instructionals", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Wisp Animus", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Crystal Ball", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Meteoric Glass", 'Collect seven runebox fragments in Sunhold in Summerset'),
            ("Psijic Glowglobe's Purified Glow Dust", 'Collect seven runebox fragments in Sunhold in Summerset'),
        ]),
    ('Grisly Mummy Tabby', 'Public Dungeon', [
            ('Mummified Alfiq Parts', 'Rimmen Necropolis in Northern Elsweyr'),
        ]),
    ('Peryite Skeevemaster', 'Public Dungeon', [
            ('Plague-Drenched Fabric', 'Find and use ten Plague-Drenched Fabrics from the Orcest in Northern Elsweyr'),
        ]),
    ('Master Field Cartographer', 'Public Dungeon', [
            ("Cartographer's Mask", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Vest", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Leggings", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Gloves", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Boots", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Tricorn", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
            ("Cartographer's Rucksack", 'Collect and combine all of the Cartographer Fragments at Nchuthnkarst in Blackreach Greymoor Caverns'),
        ]),
    ('Target Stone Husk', 'Public Dungeon', [
            ('Stone Husk Fragment', 'Combine Stone Husk Fragments found in Labyrinthian in Western Skyrim'),
        ]),
    ('Thrafey Debutante Gown', 'Public Dungeon', [
            ('Scaly Cloth Scrap', 'Silent Halls in Blackwood'),
        ]),
    ('Replica Zenithar Adytum Gate', 'Public Dungeon', [
            ('Inscribed Shard', "Zenithar's Abbey in Blackwood"),
        ]),
    ('Coral Haj Mota', 'Public Dungeon', [
            ('Coral Haj Mota Decoy', 'Spire of the Crimson Coin'),
            ('Coral Haj Mota Lure', 'Ghost Haven Bay'),
        ]),
    ('Graht-Oak Squirrel', 'Public Dungeon', [
            ('Lost Graht-Oak Acorn', 'Gorne'),
            ('Unearthed Valenwood Seedling', 'The Underweave'),
        ]),
    ('Echo of the Abolisher', 'Public Dungeon', [
            ('Remnant of Deception', 'Silorn'),
            ('Remnant of Cruelty', 'Leftwheal Trading Post'),
        ]),
    ('Eviscerate, Violet Purple', 'Public Dungeon', [
            ('Phial of Tainted Blood', 'Acquire and use 25 Phials of Tainted Blood drop from enemies in the Deetra Grotto Public Dungeon located in Solstice'),
        ]),
    ('Soul Trap, Wormwrithe', 'Public Dungeon', [
            ('Worm-Touched Soul Gem', 'Obtain and use 25 Worm-Touched Soul Gems in the Calindvale Gardens in Eastern Solstice.'),
        ]),

    # --- Event ---
    ('Apple-Bobbing Cauldron', 'Event', [
            ('Apple-Bobbing Fresh Gorapples', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Cold Iron Cauldron', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Aged Fetid Fish', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Stale Creek Water', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Poise Guide', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Viscous Slime', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
            ('Apple-Bobbing Fenwood Ladle', 'Collect the Apple-Bobbing memento pieces available during the 2018 Witches Festival'),
        ]),
    ('Alliance Breton Terrier', 'Event', [
            ('Breton Terrier Mammoth Bone', "As a Daggerfall Covenant character, collect and combine ten Breton Terrier Mammoth Bones found inside Pelinal's Midyear Boon Boxes (2021) or bought from the Impresario"),
        ]),
    ("Cadwell's Surprise Box", 'Event', [
            ('Revelry Shard', "Combine 5 Revelry Shards which can be obtained from Jester's Festival Boxes or bought from the Impresario during the 2022 Jester's Festival"),
        ]),
    ('Festive Noise Maker', 'Event', [
            ('Festive Noise Maker Parts', "Consume 5 Festive Noise Maker Parts found in Stupendous Jester's Festival Boxes"),
        ]),
    ("Jester's Festival Joke Popper", 'Event', [
            ('Joke Popper Parts', "Consume 5 Joke Popper Parts found in Stupendous Jester's Festival Boxes"),
        ]),
    ('Microtized Verminous Fabricant', 'Event', [
            ('Sealed Fabrication Materials', 'Combine ten Sealed Fabrication Materials found during the Pan-Tamriel Celebration (Jan 23 - Feb 4, 2025), obtained through Pan-Tamriel Reward Boxes or purchased from Philius Dormier with Event Tickets'),
        ]),
    ("Playful Prankster's Surprise Box", 'Event', [
            ('Mirth Shard', "Combine 5 Mirth Shards which can be obtained from Jester's Festival Boxes or bought from the Impresario"),
        ]),
    ('Skeletal Marionette', 'Event', [
            ('Skeletal Marionette Parts', 'Consume ten Skeletal Marionette Parts, found in all varieties of Plunder Skull during the 2019 Witches Festival'),
        ]),
    ('Sovereign Sow', 'Event', [
            ('Sovereign Brush', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Fodder', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Lead', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Libations', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Oil', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Sash', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
            ('Sovereign Tiara', "Find and combine all seven Sovereign Sow collectible fragments found in Stupendous Jester's Festival Boxes during the 2020 Jester's Festival"),
        ]),
    ('Throwing Bones', 'Event', [
            ('Rune-Carved Bone Fragment', 'Assemble a set of 10 Rune-Carved Bone Fragments, dropped from Plunder Skulls during the Witches Festival (introduced 2020)'),
        ]),
    ('Voriplasm', 'Event', [
            ('Voriplasm Trap: Compliance Oil', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: Crystal Jar', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: Enticing Bait', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: Gold Spring', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: Training Salts', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: Trigger Wire', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
            ('Voriplasm Trap: User Manual', 'Find and use seven Voriplasm Trap parts, found in Murkmire Strongboxes or bought from the Impresario during the Murkmire Celebration and the Bounties of Blackwood event'),
        ]),
    ('Wooden Grave-Stake', 'Event', [
            ('Grave Stake: Attuned Bonework', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Blessed Carved Wood', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Blooded Pigments', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Consecrated Mud', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Hallowed Leather', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Ritual Instructions', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
            ('Grave Stake: Sacred Binding', 'Collect all seven Grave Stake fragments from Murkmire Strongboxes during the 2020 Murkmire Celebration event, or purchased from Philius Dormier in Alinor for 1 Event Ticket each during the 2025 Pan-Tamriel Celebration'),
        ]),

    # --- Prologue Quest ---
    ('Swamp Jelly', 'Prologue Quest', [
            ('Swamp Jelly Fine-Mesh Net', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ('Swamp Jelly Luminous Fishmeal', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ('Swamp Jelly Luring Flute', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ('Swamp Jelly Carrying Jar', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ('Swamp Jelly Spawning Mud', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ('Swamp Jelly Moss Bedding', 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
            ("Swamp Jelly Hunter's Lens", 'Collect seven runebox fragments from Cyrodilic Collections daily jobs in Stormhold'),
        ]),
    ('Guar Stomp', 'Prologue Quest', [
            ('Guar Stomp Elucidating Hand-Sculpture', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp History in Street Theatre', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp Illustrated Reports', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp Noise Reports', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp Rehearsal Tuning Fork', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp Skeletal Reconstruction', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
            ('Guar Stomp Steps-Practice Rug', 'Find and combine seven Runebox Fragments in Northern Elsweyr Defense Force Cache containers'),
        ]),

    # --- Tales of Tribute ---
    ('Ansei Frandar Hunding Deck', 'Tales of Tribute', [
            ("Delver's Ansei Deck Fragment", 'Delves in the High Isle zone'),
            ("Slayer's Ansei Deck Fragment", 'World Bosses in the High Isle zone'),
            ("Geomancer's Ansei Deck Fragment", 'Volcanic vents in the High Isle zone'),
            ("Hero's Ansei Deck Fragment", 'Bosses in Ghost Haven Bay and the Spire of the Crimson Coin'),
            ("Diplomat's Ansei Deck Fragment", 'Quest: A Chance for Peace'),
        ]),
    ('Sorcerer-King Orgnum Deck', 'Tales of Tribute', [
            ("Author's Maormer Deck Fragment", 'Beating The Author in Tales of Tribute'),
            ("Fillia's Maormer Deck Fragment", 'Beating Fillia in Tales of Tribute'),
            ("Linyia's Maormer Deck Fragment", 'Beating Linyia in Tales of Tribute'),
            ("Murzaga's Maormer Deck Fragment", 'Beating Murzaga gra-Ghorn in Tales of Tribute'),
            ("Nhorhim's Maormer Deck Fragment", 'Beating Nhorhim in Tales of Tribute'),
        ]),
    ('Druid King Deck', 'Tales of Tribute', [
            ("Delver's Druid Deck Fragment", 'Delves in the Galen zone'),
            ("Dreamer's Druid Deck Fragment", 'Quest: The Dream of Kasorayn'),
            ("Geomancer's Druid Deck Fragment", 'Volcanic vents in the Galen zone'),
            ("Slayer's Druid Deck Fragment", 'World Bosses in the Galen zone'),
            ('Soothing Druid Deck Fragment', 'Quest: The Best of Friends'),
        ]),
    ('Almalexia Deck', 'Tales of Tribute', [
            ("Academ's Almalexia Deck Fragment", "Quest: Herald's Seekers"),
            ("Delver's Almalexia Deck Fragment", 'Delves on the Telvanni Peninsula and in Apocrypha'),
            ("Hero's Almalexia Deck Fragment", 'Bosses from Gorne and The Underweave'),
            ("Seeker's Almalexia Deck Fragment", "Quest: Llaro's Headache"),
            ("Slayer's Almalexia Deck Fragment", 'World Bosses on the Telvanni Peninsula and in Apocrypha'),
        ]),
    ('Hermaeus Mora Deck', 'Tales of Tribute', [
            ("Academ's Mora Deck Fragment", 'Infinite Archive'),
            ("Delver's Mora Deck Fragment", 'Infinite Archive'),
            ("Filer's Mora Deck Fragment", 'Purchased from Filer Tezurs for Data (amount not listed on wiki)'),
            ("Seeker's Mora Deck Fragment", 'Infinite Archive'),
            ("Slayer's Mora Deck Fragment", 'Infinite Archive'),
        ]),
    ('Saint Alessia Deck', 'Tales of Tribute', [
            ("Delver's Alessia Deck Fragment", 'Delve Bosses in West Weald'),
            ("Hero's Alessia Deck Fragment", 'Bosses from Leftwheal Trading Post and Silorn'),
            ('Shattered Alessia Deck Fragment', 'Mirrormoor Incursions'),
            ("Seeker's Alessia Deck Fragment", 'Quest: The Untraveled Road'),
            ("Slayer's Alessia Deck Fragment", 'World Bosses in West Weald'),
        ]),
    ('Captain Kaleen', 'Tales of Tribute', [
            ("Scrap of the Spearhead's Colors", "Use 10 Scraps of the Spearhead's Colors, acquired from Tales of Tribute match rewards"),
        ]),
    ('Card Conjuring', 'Tales of Tribute', [
            ('Heavily Played Tribute Card', "Complete the achievement 'Card Conjurer'"),
        ]),

    # --- Infinite Archive ---
    ('Maligraphic Mount', 'Infinite Archive', [
            ('Maligraphic Ichor', 'Replication Elimination; or purchased from Filer Ool for Data (amount not listed on wiki)'),
        ]),
    ('Maligraphic Skeever', 'Infinite Archive', [
            ('Disgusting Spoils', 'Muniment Chests; or purchased from Filer Ool for Data (amount not listed on wiki)'),
        ]),
    ('Shattered Mirror Maze Body Marks', 'Infinite Archive', [
            ('Erroneous Archive Map', 'Theater of War; or purchased from Filer Ool for Data (amount not listed on wiki)'),
        ]),
    ('Shattered Mirror Maze Face Marks', 'Infinite Archive', [
            ('Unreliable Archive Map', 'Treacherous Crossing; or purchased from Filer Ool for Data (amount not listed on wiki)'),
        ]),
    ('Veteran of the Infinite Body Art', 'Infinite Archive', [
            ('Archival Riddles', None),
        ]),
    ('Veteran of the Infinite Face Art', 'Infinite Archive', [
            ('Archival Enigmas', None),
        ]),

    # --- Skill Style ---
    ('Mosaic Skill Shred Skill Styles', 'Skill Style', [
            ('Mosaic Skill Shred', 'Acquire and use 20 Mosaic Style Shreds from Mirrormoor Incursions at West Weald Mosaics'),
        ]),
    ('Cleave, Cinnabar Red', 'Skill Style', [
            ('Class Script Scrap', 'Acquired by completing the "A Signature with Class" achievement'),
        ]),
    ('Annulment, Vibrant Yellow', 'Skill Style', [
            ('Fragment of Balamath', 'Looted from Corrupted Scion of Balamath in Balamath'),
            ('Fragment of Rulanyil', "Looted from Hergor the Fallen in Rulanyil's Fall"),
            ('Fragment of the Crazed', 'Looted from Sthorha the Crazed at Aba Darre'),
            ('Fragment of the Scrivener', "Looted from Valinna in Scrivener's Hall"),
            ('Fragment of Madness', 'Looted from The Mad Architect in Vaults of Madness'),
        ]),
    ('Force Shock, Wildburn', 'Skill Style', [
            ('Fragment of Aggression', 'Looted from Aggression of Root in Haldain Lumber Camp'),
            ('Fragment of the Weald', 'Looted from Yrrkkyyn in Leftwheal Trading Post'),
            ('Fragment of the Fate-Eater', 'Looted from Stri the Fate-Eater in Broken Path Cave'),
            ('Fragment of the Blind', 'Looted from The Blind in Bedlam Veil'),
            ('Fragment of the Storm', 'Looted from Stormreeve Neidir in Tempest Island'),
            ('Fragment of the Maw', 'Looted from Rakkhat in Maw of Lorkhaj'),
        ]),
    ('Mist Form, Lilac Purple', 'Skill Style', [
            ('Fragment of the Voracious', 'Looted from Thaliel the Voracious at Molavar Delve in Craglorn'),
            ('Fragment of the Ratmaster', "Looted from Olveidi the Ratmaster at Ratmaster's Prowl group boss in Eastmarch"),
            ('Fragment of the Alchemist', 'Looted from Arkasis the Mad Alchemist at Stone Garden in Blackreach'),
            ('Fragment of the Hollowfang', 'Looted from Grundwulf at Moongrave Fane in Northern Elsweyr'),
            ('Fragment of the Vampire Lord', "Looted from Lord Falgravn at Kyne's Aegis in Western Skyrim"),
        ]),
    ('Puncture, Lavaburst', 'Skill Style', [
            ('Fragment of the Martyr', "Looted from Kurkron the Mangler in False Martyr's Folly"),
            ('Fragment of the Forgotten', 'Looted from the Group Event Bosses in Forgotten Wastes'),
            ('Fragment of the Vents', 'Looted from Volcanic Cache after defeating the final Boss of the Systres Volcanic Vents'),
            ('Fragment of the Baron', 'Looted from Baron Zaudrus in The Cauldron'),
            ('Fragment of Ash', 'Looted from Valkyn Skoria in City of Ash II'),
            ('Fragment of the Sunspire', 'Looted from Nahviintaas in Sunspire'),
        ]),
    ('Roar, Verdant Green', 'Skill Style', [
            ('Fragment of Hircine', "Looted from Packleader Sigmund in Hircine's Haunt"),
            ('Fragment of the Bad Man', "Looted from Skitterflame in Bad Man's Hallows"),
            ('Fragment of the Wolf-Father', 'Looted from Garach Wolf-Father at Lakewatch Tower'),
            ('Fragment of the Crucible', 'Looted from The Lava Queen in Blessed Crucible'),
            ('Fragment of the Ascendant', 'Looted from Vykosa the Ascendant in Moon Hunter Keep'),
        ]),
    ('Silver Bolts, Vibrant Yellow', 'Skill Style', [
            ('Fragment of the Black Maw', 'Looted from Peers-Through-Glass in Shrine of the Black Maw'),
            ('Fragment of the Obsidian Scar', 'Looted from Zilbash the Deceiver in Obsidian Scar'),
            ('Fragment of the Exarch', 'Looted from Exarch Savfyr at Vampire Feeding Grounds'),
            ('Fragment of the Winterbourne', 'Looted from Vorenor Winterbourne in Spindleclutch II'),
            ('Fragment of the Thorn', 'Looted from Lady Thorn in Castle Thorn'),
        ]),
    ('Soul Trap, Carmine Red', 'Skill Style', [
            ('Harvested Soul Fragment', 'Looted from Worm Cult Champions during Soul Reaper incursions'),
        ]),
]

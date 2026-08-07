"""
ESO provisioning recipe seed data from game data.
Format: (name, ri, rq, food_level, dish_type, health, magicka, stamina,
         ing_meat, ing_fruit, ing_veg, ing_med, ing_impr, duration_mins)
  ri        = Recipe Improvement passive level required (1-6)
  rq        = Recipe quality tier (1-3)
  food_level= Character / scaling level
  ing_*     = Ingredient category required in that slot (None = unused)
  ing_impr  = Improvement ingredient (Frost Mirriam for Gourmet only)
  duration  = Buff duration in minutes
"""

RECIPES = [
    # ── Level 1, RI 1, RQ 1 ──────────────────────────────────────────────────
    ("Chicken Breast",         1,1,1,  "Meat",      743,   0,   0, "Poultry",    None,           None,     None,        None,           35),
    ("Fishy Stick",            1,1,1,  "Meat",      743,   0,   0, "Fish",       None,           None,     None,        None,           35),
    ("Roast Pig",              1,1,1,  "Meat",      743,   0,   0, "White Meat", None,           None,     None,        None,           35),
    ("Baked Apples",           1,1,1,  "Fruit",       0, 680,   0, None,         "Apples",       None,     None,        None,           35),
    ("Banana Surprise",        1,1,1,  "Fruit",       0, 680,   0, None,         "Bananas",      None,     None,        None,           35),
    ("Grape Preserves",        1,1,1,  "Fruit",       0, 680,   0, None,         "Jazbay Grapes",None,     None,        None,           35),
    ("Baked Potato",           1,1,1,  "Vegetable",   0,   0, 680, None,         None,           "Potato", None,        None,           35),
    ("Carrot Soup",            1,1,1,  "Vegetable",   0,   0, 680, None,         None,           "Carrots",None,        None,           35),
    ("Roast Corn",             1,1,1,  "Vegetable",   0,   0, 680, None,         None,           "Corn",   None,        None,           35),

    # ── Level 5, RI 1, RQ 1 ──────────────────────────────────────────────────
    ("plank Steak",            1,1,5,  "Meat",     1156,   0,   0, "Red Meat",   None,           None,     None,        None,           35),
    ("Grilled Hare",           1,1,5,  "Meat",     1156,   0,   0, "Small Game", None,           None,     None,        None,           35),
    ("Roast Venison",          1,1,5,  "Meat",     1156,   0,   0, "Game",       None,           None,     None,        None,           35),
    ("Melon Jelly",            1,1,5,  "Fruit",       0,1058,   0, None,         "Melon",        None,     None,        None,           35),
    ("Pumpkin Puree",          1,1,5,  "Fruit",       0,1058,   0, None,         "Pumpkin",      None,     None,        None,           35),
    ("Tomato Soup",            1,1,5,  "Fruit",       0,1058,   0, None,         "Tomato",       None,     None,        None,           35),
    ("Borscht",                1,1,5,  "Vegetable",   0,   0,1058, None,         None,           "Beets",  None,        None,           35),
    ("Green Salad",            1,1,5,  "Vegetable",   0,   0,1058, None,         None,           "Greens", None,        None,           35),
    ("Steamed Radishes",       1,1,5,  "Vegetable",   0,   0,1058, None,         None,           "Radish", None,        None,           35),

    # ── Level 10, RI 1, RQ 1 ─────────────────────────────────────────────────
    ("Hunter's Pie",           1,1,10, "Meat",     1569,   0,   0, "Game",       None,           None,     "Saltrice",  None,           35),
    ("Rabbit Pasty",           1,1,10, "Meat",     1569,   0,   0, "Small Game", None,           None,     "Flour",     None,           35),
    ("Tarragon Chicken",       1,1,10, "Meat",     1569,   0,   0, "Poultry",    None,           None,     "Seasoning", None,           35),
    ("Banana Millet Muffin",   1,1,10, "Fruit",       0,1436,   0, None,         "Bananas",      None,     "Millet",    None,           35),
    ("Bravil Melon Salad",     1,1,10, "Fruit",       0,1436,   0, None,         "Melon",        None,     "Garlic",    None,           35),
    ("Pumpkin Cheesecake",     1,1,10, "Fruit",       0,1436,   0, None,         "Pumpkin",      None,     "Cheese",    None,           35),
    ("Carrot Cheesecake",      1,1,10, "Vegetable",   0,   0,1436, None,         None,           "Carrots","Cheese",    None,           35),
    ("Gilane Garlicky Greens", 1,1,10, "Vegetable",   0,   0,1436, None,         None,           "Greens", "Garlic",    None,           35),
    ("Radishes in Rice",       1,1,10, "Vegetable",   0,   0,1436, None,         None,           "Radish", "Saltrice",  None,           35),

    # ── Level 10, RI 1, RQ 2 ─────────────────────────────────────────────────
    ("Melon Carpaccio",           1,2,10, "Savoury",  1381,1264,   0, "Red Meat",   "Melon",        None,     None,        None,           60),
    ("Punkin Bunny",              1,2,10, "Savoury",  1381,1264,   0, "Small Game", "Pumpkin",      None,     None,        None,           60),
    ("Red Deer Stew",             1,2,10, "Savoury",  1381,1264,   0, "Game",       "Tomato",       None,     None,        None,           60),
    ("Beet-Glazed Pork",          1,2,10, "Ragout",   1381,   0,1264, "White Meat", None,          "Beets",  None,        None,           60),
    ("Salmon with Radish Slaw",   1,2,10, "Ragout",   1381,   0,1264, "Fish",       None,          "Radish", None,        None,           60),
    ("Stuffed Capon",             1,2,10, "Ragout",   1381,   0,1264, "Poultry",    None,          "Corn",   None,        None,           60),
    ("Last Seed Salad",           1,2,10, "Entremet",    0,1264,1264, None,         "Apples",      "Carrots",None,        None,           60),
    ("Mid Year Green Salad",      1,2,10, "Entremet",    0,1264,1264, None,         "Jazbay Grapes","Greens",None,        None,           60),
    ("Sweet Potatoes",            1,2,10, "Entremet",    0,1264,1264, None,         "Bananas",     "Potato", None,        None,           60),

    # ── Level 15, RI 1, RQ 1 ─────────────────────────────────────────────────
    ("Pan-Fried Trout",                     1,1,15, "Meat",      1982,   0,   0, "Fish",       None,           None,     "Flour",     None,           35),
    ("Rabbit Millet Pilaf",                 1,1,15, "Meat",      1982,   0,   0, "Small Game", None,           None,     "Millet",    None,           35),
    ("Stir-Fried Garlic Beef",              1,1,15, "Meat",      1982,   0,   0, "Red Meat",   None,           None,     "Garlic",    None,           35),
    ("Deshaan Honeydew Hors D'oeuvres",     1,1,15, "Fruit",        0,1814,   0, None,         "Melon",        None,     "Saltrice",  None,           35),
    ("Fried Green Tomatoes",                1,1,15, "Fruit",        0,1814,   0, None,         "Tomato",       None,     "Seasoning", None,           35),
    ("Stuffed Grape Leaves",                1,1,15, "Fruit",        0,1814,   0, None,         "Jazbay Grapes",None,     "Millet",    None,           35),
    ("Balmora Cabbage Biscuits",            1,1,15, "Vegetable",    0,   0,1814, None,         None,           "Greens", "Flour",     None,           35),
    ("Port Hunding Cheese Fries",           1,1,15, "Vegetable",    0,   0,1814, None,         None,           "Potato", "Cheese",    None,           35),
    ("Spicy Beet Salad",                    1,1,15, "Vegetable",    0,   0,1814, None,         None,           "Beets",  "Seasoning", None,           35),

    # ── Level 15, RI 1, RQ 2 ─────────────────────────────────────────────────
    ("Apple Baked Fish",                1,2,15, "Savoury",  1710,1565,   0, "Fish",       "Apples",       None,     None,        None,           60),
    ("Grape-Glazed Bantam Guar",        1,2,15, "Savoury",  1710,1565,   0, "Poultry",    "Jazbay Grapes",None,     None,        None,           60),
    ("Monkeypig Cutlets",               1,2,15, "Savoury",  1710,1565,   0, "White Meat", "Bananas",      None,     None,        None,           60),
    ("Beef Stew",                       1,2,15, "Ragout",   1710,   0,1565, "Red Meat",   None,           "Carrots",None,        None,           60),
    ("Rabbit Loin with Bitter Greens",  1,2,15, "Ragout",   1710,   0,1565, "Small Game", None,           "Greens", None,        None,           60),
    ("Shepherd's Pie",                  1,2,15, "Ragout",   1710,   0,1565, "Game",       None,           "Potato", None,        None,           60),
    ("Melon-Radish Salad",              1,2,15, "Entremet",    0,1565,1565, None,         "Melon",        "Radish", None,        None,           60),
    ("Pumpkin Corn Fritters",           1,2,15, "Entremet",    0,1565,1565, None,         "Pumpkin",      "Corn",   None,        None,           60),
    ("Tomato Borscht",                  1,2,15, "Entremet",    0,1565,1565, None,         "Tomato",       "Beets",  None,        None,           60),

    # ── Level 20, RI 2, RQ 1 ─────────────────────────────────────────────────
    ("Breton Pork Sausage",             2,1,20, "Meat",      2395,   0,   0, "White Meat", None,           None,     "Seasoning", None,           35),
    ("Venison Pasty",                   2,1,20, "Meat",      2395,   0,   0, "Game",       None,           None,     "Flour",     None,           35),
    ("Whiterun Cheese-Baked Trout",     2,1,20, "Meat",      2395,   0,   0, "Fish",       None,           None,     "Cheese",    None,           35),
    ("Garlic Pumpkin Seeds",            2,1,20, "Fruit",        0,2192,   0, None,         "Pumpkin",      None,     "Garlic",    None,           35),
    ("Pellitine Tomato Rice",           2,1,20, "Fruit",        0,2192,   0, None,         "Tomato",       None,     "Saltrice",  None,           35),
    ("Redoran Peppered Melon",          2,1,20, "Fruit",        0,2192,   0, None,         "Melon",        None,     "Seasoning", None,           35),
    ("Alik'r Beets with Goat Cheese",   2,1,20, "Vegetable",    0,   0,2192, None,         None,           "Beets",  "Cheese",    None,           35),
    ("Battaglir Chowder",               2,1,20, "Vegetable",    0,   0,2192, None,         None,           "Greens", "Millet",    None,           35),
    ("Nibenese Garlic Carrots",         2,1,20, "Vegetable",    0,   0,2192, None,         None,           "Carrots","Garlic",    None,           35),

    # ── Level 20, RI 2, RQ 2 ─────────────────────────────────────────────────
    ("Argonian Pumpkin Stew",       2,2,20, "Savoury",  2039,1866,   0, "Fish",       "Pumpkin",      None,     "Saltrice",  None,           60),
    ("Peacock Pie",                 2,2,20, "Savoury",  2039,1866,   0, "Poultry",    "Jazbay Grapes",None,     "Flour",     None,           60),
    ("Yellow Oxen Loaf",            2,2,20, "Savoury",  2039,1866,   0, "Red Meat",   "Bananas",      None,     "Millet",    None,           60),
    ("Beef and Beets Pasty",        2,2,20, "Ragout",   2039,   0,1866, "Red Meat",   None,           "Beets",  "Millet",    None,           60),
    ("Rabbit Gnocchi Ragu",         2,2,20, "Ragout",   2039,   0,1866, "Small Game", None,           "Potato", "Flour",     None,           60),
    ("Stuffed Venison Haunch",      2,2,20, "Ragout",   2039,   0,1866, "Game",       None,           "Greens", "Cheese",    None,           60),
    ("Falinesti Forbidden Fruit",   2,2,20, "Entremet",    0,1866,1866, None,         "Melon",        "Radish", "Seasoning", None,           60),
    ("Hearthfire Harvest Pilaf",    2,2,20, "Entremet",    0,1866,1866, None,         "Apples",       "Corn",   "Saltrice",  None,           60),
    ("Hearty Sun's Dusk Soup",      2,2,20, "Entremet",    0,1866,1866, None,         "Tomato",       "Carrots","Garlic",    None,           60),

    # ── Level 20, RI 2, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Corinthe Corn Beef",  2,3,20, "Gourmet",  1785,1642,1642, "Red Meat", "Bananas",  "Corn",   None, "Frost Mirriam", 120),

    # ── Level 25, RI 2, RQ 1 ─────────────────────────────────────────────────
    ("Cheese Pork Schnitzel",           2,1,25, "Meat",      2808,   0,   0, "White Meat", None,           None,     "Cheese",    None,           35),
    ("Chicken and Biscuits",            2,1,25, "Meat",      2808,   0,   0, "Poultry",    None,           None,     "Millet",    None,           35),
    ("Salted Cod",                      2,1,25, "Meat",      2808,   0,   0, "Fish",       None,           None,     "Seasoning", None,           35),
    ("Cantaloupe Bread",                2,1,25, "Fruit",        0,2570,   0, None,         "Melon",        None,     "Flour",     None,           35),
    ("Cinnamon Gorapples",              2,1,25, "Fruit",        0,2570,   0, None,         "Apples",       None,     "Seasoning", None,           35),
    ("Green Bananas with Garlic",       2,1,25, "Fruit",        0,2570,   0, None,         "Bananas",      None,     "Garlic",    None,           35),
    ("Eidar Radish Salad",              2,1,25, "Vegetable",    0,   0,2570, None,         None,           "Radish", "Cheese",    None,           35),
    ("Potato Rice Blintzes",            2,1,25, "Vegetable",    0,   0,2570, None,         None,           "Potato", "Saltrice",  None,           35),
    ("Rihad Beet and Garlic Salad",     2,1,25, "Vegetable",    0,   0,2570, None,         None,           "Beets",  "Garlic",    None,           35),

    # ── Level 25, RI 2, RQ 2 ─────────────────────────────────────────────────
    ("Baked Sole with Bananas",         2,2,25, "Savoury",  2368,2167,2167, "Fish",       "Bananas",      None,     "Flour",     None,           60),
    ("Colovian Roast Turkey",           2,2,25, "Savoury",  2368,2167,   0, "Poultry",    "Tomato",       None,     "Millet",    None,           60),
    ("Pork and Bitter Melon",           2,2,25, "Savoury",  2368,2167,   0, "White Meat", "Melon",        None,     "Saltrice",  None,           60),
    ("Falkreath Meat Loaf",             2,2,25, "Ragout",   2368,   0,2167, "Game",       None,           "Carrots","Cheese",    None,           60),
    ("Highland Rabbit Stew",            2,2,25, "Ragout",   2368,   0,2167, "Small Game", None,           "Greens", "Millet",    None,           60),
    ("Hunt-Wife's Beef Radish Stew",    2,2,25, "Ragout",   2368,   0,2167, "Red Meat",   None,           "Radish", "Seasoning", None,           60),
    ("Apple Mashed Potatoes",           2,2,25, "Entremet",    0,2167,2167, None,         "Apples",       "Potato", "Garlic",    None,           60),
    ("Elsweyr Corn Fritters",           2,2,25, "Entremet",    0,2167,2167, None,         "Jazbay Grapes","Corn",   "Flour",     None,           60),
    ("Hearthfire Vegetable Salad",      2,2,25, "Entremet",    0,2167,2167, None,         "Pumpkin",      "Beets",  "Saltrice",  None,           60),

    # ── Level 25, RI 2, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Sweet Skeever Gumbo",  2,3,25, "Gourmet",  2047,1883,1883, "Small Game", "Apples",  "Beets",  None, "Frost Mirriam", 120),

    # ── Level 30, RI 3, RQ 1 ─────────────────────────────────────────────────
    ("Elinhir Roast Antelope",      3,1,30, "Meat",      3221,   0,   0, "Game",       None,           None,     "Millet",    None,           35),
    ("Hare in Garlic Sauce",        3,1,30, "Meat",      3221,   0,   0, "Small Game", None,           None,     "Garlic",    None,           35),
    ("Senchal Curry Fish and Rice", 3,1,30, "Meat",      3221,   0,   0, "Fish",       None,           None,     "Saltrice",  None,           35),
    ("Stormhold Baked Bananas",     3,1,30, "Fruit",        0,2948,   0, None,         "Bananas",      None,     "Cheese",    None,           35),
    ("Cinnamon Grape Jelly",        3,1,30, "Fruit",        0,2948,   0, None,         "Jazbay Grapes",None,     "Seasoning", None,           35),
    ("Cyrodilic Pumpkin Fritters",  3,1,30, "Fruit",        0,2948,   0, None,         "Pumpkin",      None,     "Millet",    None,           35),
    ("Chorrol Corn on the Cob",     3,1,30, "Vegetable",    0,   0,2948, None,         None,           "Corn",   "Seasoning", None,           35),
    ("Garlic Mashed Potatoes",      3,1,30, "Vegetable",    0,   0,2948, None,         None,           "Potato", "Garlic",    None,           35),
    ("Jerall View Inn Carrot Cake", 3,1,30, "Vegetable",    0,   0,2948, None,         None,           "Carrots","Flour",     None,           35),

    # ── Level 30, RI 3, RQ 2 ─────────────────────────────────────────────────
    ("Parmesan Eels in Watermelon", 3,2,30, "Savoury",  2697,2468,   0, "Fish",       "Melon",        None,     "Cheese",    None,           60),
    ("Pumpkin-Stuffed Fellrunner",  3,2,30, "Savoury",  2697,2468,   0, "Poultry",    "Pumpkin",      None,     "Saltrice",  None,           60),
    ("Redguard Venison Pie",        3,2,30, "Savoury",  2697,2468,   0, "Game",       "Tomato",       None,     "Flour",     None,           60),
    ("Frostfall Pork Roast",        3,2,30, "Ragout",   2697,   0,2468, "White Meat", None,           "Radish", "Seasoning", None,           60),
    ("Rabbit Corn Chowder",         3,2,30, "Ragout",   2697,   0,2468, "Small Game", None,           "Corn",   "Saltrice",  None,           60),
    ("Shornhelm Ox-Tail Soup",      3,2,30, "Ragout",   2697,   0,2468, "Red Meat",   None,           "Carrots","Millet",    None,           60),
    ("Apple-Eidar Cheese Salad",    3,2,30, "Entremet",    0,2468,2468, None,         "Apples",       "Greens", "Cheese",    None,           60),
    ("Sun's Height Pudding",        3,2,30, "Entremet",    0,2468,2468, None,         "Bananas",      "Beets",  "Garlic",    None,           60),
    ("Sweet Dune Gnocchi",          3,2,30, "Entremet",    0,2468,2468, None,         "Jazbay Grapes","Potato", "Flour",     None,           60),

    # ── Level 30, RI 3, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Riekling Suckling Bristleback", 3,3,30, "Gourmet", 2310,2125,2125, "White Meat","Pumpkin","Greens",None,"Frost Mirriam",120),

    # ── Level 35, RI 3, RQ 1 ─────────────────────────────────────────────────
    ("Bruma Jugged Rabbit",          3,1,35, "Meat",      3634,   0,   0, "Small Game", None,           None,     "Seasoning", None,           35),
    ("Camlorn Pork Sausage",         3,1,35, "Meat",      3634,   0,   0, "White Meat", None,           None,     "Garlic",    None,           35),
    ("Crispy Cheddar Chicken",       3,1,35, "Meat",      3634,   0,   0, "Poultry",    None,           None,     "Cheese",    None,           35),
    ("Apple Cobbler Supreme",        3,1,35, "Fruit",        0,3326,   0, None,         "Apples",       None,     "Flour",     None,           35),
    ("Clan Mother's Banana Pilaf",   3,1,35, "Fruit",        0,3326,   0, None,         "Bananas",      None,     "Saltrice",  None,           35),
    ("Rimmen Raisin Cookies",        3,1,35, "Fruit",        0,3326,   0, None,         "Jazbay Grapes",None,     "Flour",     None,           35),
    ("Indoril Radish Tartlets",      3,1,35, "Vegetable",    0,   0,3326, None,         None,           "Radish", "Flour",     None,           35),
    ("Roasted Beet and Millet Salad",3,1,35, "Vegetable",    0,   0,3326, None,         None,           "Beets",  "Millet",    None,           35),
    ("Twice-Baked Potatoes",         3,1,35, "Vegetable",    0,   0,3326, None,         None,           "Potato", "Seasoning", None,           35),

    # ── Level 35, RI 3, RQ 2 ─────────────────────────────────────────────────
    ("Aunt Alessia's Pork Chops",        3,2,35, "Savoury",  3026,2769,   0, "White Meat", "Tomato",       None,     "Garlic",    None,           60),
    ("Minotaur Slumgullion",             3,2,35, "Savoury",  3026,2769,   0, "Red Meat",   "Pumpkin",      None,     "Millet",    None,           60),
    ("Venison Stuffed Grape Leaves",     3,2,35, "Savoury",  3026,2769,   0, "Game",       "Jazbay Grapes",None,     "Saltrice",  None,           60),
    ("Fricasseed Rabbit with Radishes",  3,2,35, "Ragout",   3026,   0,2769, "Small Game", None,           "Radish", "Seasoning", None,           60),
    ("Mudcrab Corn Fritters",            3,2,35, "Ragout",   3026,   0,2769, "Fish",       None,           "Corn",   "Garlic",    None,           60),
    ("Narsis Bantam Guar Hash",          3,2,35, "Ragout",   3026,   0,2769, "Poultry",    None,           "Beets",  "Saltrice",  None,           60),
    ("Blackwood Stuffed Banana Leaves",  3,2,35, "Entremet",    0,2769,2769, None,         "Bananas",      "Greens", "Millet",    None,           60),
    ("Creamcheese Frosted Gorapple Cake",3,2,35, "Entremet",    0,2769,2769, None,         "Apples",       "Carrots","Cheese",    None,           60),
    ("Forge-Wife's Spudmelon Pie",       3,2,35, "Entremet",    0,2769,2769, None,         "Melon",        "Potato", "Flour",     None,           60),

    # ── Level 35, RI 3, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Dawnstar Sun's Dusk Chowder",    3,3,35, "Gourmet", 2572,2366,2366, "Red Meat",  "Pumpkin", "Corn",   None,"Frost Mirriam",120),
    ("Nibenese Fricasseed Fawn",       3,3,35, "Gourmet", 2572,2366,2366, "Game",      "Apples",  "Greens", None,"Frost Mirriam",120),
    ("Summerset Rainbow Pie",          3,3,35, "Gourmet", 2572,2366,2366, "Small Game","Bananas", "Beets",  None,"Frost Mirriam",120),
    ("Vvardenfell Cliff Racer Ragout", 3,3,35, "Gourmet", 2572,2366,2366, "Poultry",   "Tomato",  "Carrots",None,"Frost Mirriam",120),

    # ── Level 40, RI 4, RQ 1 ─────────────────────────────────────────────────
    ("Mammoth Snout Pie",               4,1,40, "Meat",      4047,   0,   0, "Red Meat",   None,           None,     "Flour",     None,           35),
    ("Rabbit Haunch with Cheese Grits", 4,1,40, "Meat",      4047,   0,   0, "Small Game", None,           None,     "Cheese",    None,           35),
    ("Stros M'Kai Grilled Seagull",     4,1,40, "Meat",      4047,   0,   0, "Poultry",    None,           None,     "Garlic",    None,           35),
    ("Kragenmoor Pickled Pumpkin",      4,1,40, "Fruit",        0,3704,   0, None,         "Pumpkin",      None,     "Seasoning", None,           35),
    ("Skyrim Jazbay Crostata",          4,1,40, "Fruit",        0,3704,   0, None,         "Jazbay Grapes",None,     "Saltrice",  None,           35),
    ("Summer Sundas Soup",              4,1,40, "Fruit",        0,3704,   0, None,         "Tomato",       None,     "Millet",    None,           35),
    ("Cheesemonger's Salad",            4,1,40, "Vegetable",    0,   0,3704, None,         None,           "Greens", "Cheese",    None,           35),
    ("Cyrodilic Cornbread",             4,1,40, "Vegetable",    0,   0,3704, None,         None,           "Corn",   "Flour",     None,           35),
    ("Toasted Millet Salad",            4,1,40, "Vegetable",    0,   0,3704, None,         None,           "Radish", "Millet",    None,           35),

    # ── Level 40, RI 4, RQ 2 ─────────────────────────────────────────────────
    ("Black Marsh Wamasu Loin",          4,2,40, "Savoury",  3355,3070,   0, "White Meat", "Jazbay Grapes",None,     "Seasoning", None,           60),
    ("Chicken-and-Banana Fried Rice",    4,2,40, "Savoury",  3355,3070,   0, "Poultry",    "Bananas",      None,     "Saltrice",  None,           60),
    ("Mother Mara's Savory Rabbit Stew", 4,2,40, "Savoury",  3355,3070,   0, "Small Game", "Tomato",       None,     "Garlic",    None,           60),
    ("Necrom Beetle-Cheese Poutine",     4,2,40, "Ragout",   3355,   0,3070, "Game",       None,           "Potato", "Cheese",    None,           60),
    ("Psijic Order Pigs-in-a-Blanket",   4,2,40, "Ragout",   3355,   0,3070, "White Meat", None,           "Corn",   "Millet",    None,           60),
    ("Rumare Slaughterfish Pie",         4,2,40, "Ragout",   3355,   0,3070, "Fish",       None,           "Greens", "Flour",     None,           60),
    ("Ashlander Ochre Mash",             4,2,40, "Entremet",    0,3070,3070, None,         "Pumpkin",      "Carrots","Seasoning", None,           60),
    ("Orcish No-Rhubarb Salad",          4,2,40, "Entremet",    0,3070,3070, None,         "Apples",       "Radish", "Garlic",    None,           60),
    ("Spinner's Taboo Salad",            4,2,40, "Entremet",    0,3070,3070, None,         "Melon",        "Beets",  "Saltrice",  None,           60),

    # ── Level 40, RI 4, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Gold Coast Mudcrab Fries", 4,3,40, "Gourmet", 2835,2608,2608, "Fish",       "Melon",        "Potato", None,"Frost Mirriam",120),
    ("Horker Loaf",              4,3,40, "Gourmet", 2835,2608,2608, "Red Meat",   "Melon",        "Corn",   None,"Frost Mirriam",120),
    ("Stirk Pork-and-Beets",     4,3,40, "Gourmet", 2835,2608,2608, "White Meat", "Bananas",      "Beets",  None,"Frost Mirriam",120),
    ("Twenty-Four-Raven Pie",    4,3,40, "Gourmet", 2835,2608,2608, "Poultry",    "Jazbay Grapes","Greens", None,"Frost Mirriam",120),

    # ── Level 45, RI 4, RQ 1 ─────────────────────────────────────────────────
    ("Akaviri Pork Fried Rice",  4,1,45, "Meat",      4460,   0,   0, "White Meat", None,           None,     "Saltrice",  None,           35),
    ("Blacklight Oxen Meatballs",4,1,45, "Meat",      4460,   0,   0, "Red Meat",   None,           None,     "Saltrice",  None,           35),
    ("Solstheim Elk and Scuttle",4,1,45, "Meat",      4460,   0,   0, "Game",       None,           None,     "Cheese",    None,           35),
    ("Mage's Gorapple Porridge", 4,1,45, "Fruit",        0,4082,   0, None,         "Apples",       None,     "Millet",    None,           35),
    ("Melon-Chevre Salad",       4,1,45, "Fruit",        0,4082,   0, None,         "Melon",        None,     "Cheese",    None,           35),
    ("Mistral Banana Bread",     4,1,45, "Fruit",        0,4082,   0, None,         "Bananas",      None,     "Flour",     None,           35),
    ("Dragonstar Radish Kebabs", 4,1,45, "Vegetable",    0,   0,4082, None,         None,           "Radish", "Seasoning", None,           35),
    ("Savory Thorn Cornbread",   4,1,45, "Vegetable",    0,   0,4082, None,         None,           "Corn",   "Saltrice",  None,           35),
    ("Vvardenfell Ash Yam Loaf", 4,1,45, "Vegetable",    0,   0,4082, None,         None,           "Potato", "Flour",     None,           35),

    # ── Level 45, RI 4, RQ 2 ─────────────────────────────────────────────────
    ("Elsweyr Fondue",                     4,2,45, "Savoury",  3684,3371,   0, "Red Meat",   "Melon",        None,     "Cheese",    None,           60),
    ("Gazelle Cutlet with Minced Pumpkin", 4,2,45, "Savoury",  3684,3371,   0, "Game",       "Pumpkin",      None,     "Seasoning", None,           60),
    ("Oyster Tomato Orzo",                 4,2,45, "Savoury",  3684,3371,   0, "Fish",       "Tomato",       None,     "Saltrice",  None,           60),
    ("Ash-Hopper Dumplings on Scathecraw", 4,2,45, "Ragout",   3684,   0,3371, "Poultry",    None,           "Greens", "Flour",     None,           60),
    ("Craglorn Skavenger Stew",            4,2,45, "Ragout",   3684,   0,3371, "Small Game", None,           "Carrots","Millet",    None,           60),
    ("Raven Rock Baked Ash Yams",          4,2,45, "Ragout",   3684,   0,3371, "White Meat", None,           "Potato", "Saltrice",  None,           60),
    ("Drunken Goat Cheese with Radishes",  4,2,45, "Entremet",    0,3371,3371, None,         "Jazbay Grapes","Radish", "Cheese",    None,           60),
    ("Savory Banana Cornbread",            4,2,45, "Entremet",    0,3371,3371, None,         "Bananas",      "Corn",   "Garlic",    None,           60),
    ("Sun-Dried Caravan Provisions",       4,2,45, "Entremet",    0,3371,3371, None,         "Apples",       "Beets",  "Seasoning", None,           60),

    # ── Level 45, RI 4, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Caramelized Goat Nibbles",           4,3,45, "Gourmet", 3097,2849,2849, "Game",      "Jazbay Grapes","Radish", None,"Frost Mirriam",120),
    ("Direnni Hundred-Year Rabbit Bisque", 4,3,45, "Gourmet", 3097,2849,2849, "Small Game","Jazbay Grapes","Corn",   None,"Frost Mirriam",120),
    ("Markarth Short Pig",                 4,3,45, "Gourmet", 3097,2849,2849, "White Meat","Apples",       "Potato", None,"Frost Mirriam",120),
    ("Parrot-and-Pumpkin Salad",           4,3,45, "Gourmet", 3097,2849,2849, "Poultry",   "Pumpkin",      "Greens", None,"Frost Mirriam",120),

    # ── Level 50, RI 5, RQ 1 ─────────────────────────────────────────────────
    ("Argonian Saddle-Cured Rabbit", 5,1,50, "Meat",      5534,   0,   0, "Small Game", None,           None,     "Saltrice",  None,           35),
    ("Dunmeri Jerked Horse Haunch",  5,1,50, "Meat",      5534,   0,   0, "Game",       None,           None,     "Seasoning", None,           35),
    ("Kwama Egg Quiche",             5,1,50, "Meat",      5534,   0,   0, "Poultry",    None,           None,     "Flour",     None,           35),
    ("Combwort Flatbread",           5,1,50, "Fruit",        0,5065,   0, None,         "Tomato",       None,     "Flour",     None,           35),
    ("Fresh Apples and Eidar Cheese",5,1,50, "Fruit",        0,5065,   0, None,         "Apples",       None,     "Cheese",    None,           35),
    ("Honey Nut Treat",              5,1,50, "Fruit",        0,5065,   0, None,         "Melon",        None,     "Millet",    None,           35),
    ("Garlic Radishes a la Kvatch",  5,1,50, "Vegetable",    0,   0,5065, None,         None,           "Radish", "Garlic",    None,           35),
    ("Pickled Carrot Slurry",        5,1,50, "Vegetable",    0,   0,5065, None,         None,           "Carrots","Saltrice",  None,           35),
    ("Skingrad Cabbage Soup",        5,1,50, "Vegetable",    0,   0,5065, None,         None,           "Greens", "Seasoning", None,           35),

    # ── Level 50, RI 5, RQ 2 ─────────────────────────────────────────────────
    ("Cloudy Dregs Inn Bouillabaisse", 5,2,50, "Savoury",  4540,4153,   0, "Fish",       "Tomato",       None,     "Flour",     None,           60),
    ("Corinthean Roast Kagouti",       5,2,50, "Savoury",  4540,4153,   0, "Red Meat",   "Apples",       None,     "Millet",    None,           60),
    ("Khajiiti Sweet-Stuffed Duck",    5,2,50, "Savoury",  4540,4153,   0, "Poultry",    "Bananas",      None,     "Cheese",    None,           60),
    ("Grandmam's Roast Rabbit",        5,2,50, "Ragout",   4540,   0,4153, "Small Game", None,           "Carrots","Saltrice",  None,           60),
    ("Hammerfell Antelope Stew",       5,2,50, "Ragout",   4540,   0,4153, "Game",       None,           "Radish", "Garlic",    None,           60),
    ("Wild-Boar-and-Beets",            5,2,50, "Ragout",   4540,   0,4153, "White Meat", None,           "Beets",  "Seasoning", None,           60),
    ("Every-Morndas Casserole",        5,2,50, "Entremet",    0,4153,4153, None,         "Melon",        "Potato", "Cheese",    None,           60),
    ("Late-Summer Corn Slaw",          5,2,50, "Entremet",    0,4153,4153, None,         "Pumpkin",      "Corn",   "Millet",    None,           60),
    ("Savory-Sweet Fried Kale",        5,2,50, "Entremet",    0,4153,4153, None,         "Jazbay Grapes","Greens", "Garlic",    None,           60),

    # ── Level 50, RI 5, RQ 3 (Gourmet) ──────────────────────────────────────
    ("Duck Soup",               5,3,50, "Gourmet", 3780,3477,3477, "Poultry",    "Tomato",       "Potato", None,"Frost Mirriam",120),
    ("Hircine's Meat Loaf",     5,3,50, "Gourmet", 3780,3477,3477, "Game",       "Apples",       "Corn",   None,"Frost Mirriam",120),
    ("Imperial Stuffed Piglet", 5,3,50, "Gourmet", 3780,3477,3477, "White Meat", "Jazbay Grapes","Radish", None,"Frost Mirriam",120),
    ("Salmon Steak Supreme",    5,3,50, "Gourmet", 3780,3477,3477, "Fish",       "Apples",       "Carrots",None,"Frost Mirriam",120),

    # ── RI 5 High-Quality Level-10 Recipes ───────────────────────────────────
    ("Curried Kwama Scrib Risotto",              5,1,10, "Meat",      4956,   0,   0, "Poultry",    None,           None,     "Saltrice",  None,           35),
    ("Grilled Timber Mammoth Kebabs",            5,1,10, "Meat",      4956,   0,   0, "Red Meat",   None,           None,     "Seasoning", None,           35),
    ("Millet-Stuffed Pork Loin",                 5,1,10, "Meat",      4956,   0,   0, "White Meat", None,           None,     "Millet",    None,           35),
    ("Hag Fen Pumpkin Pie",                      5,1,10, "Fruit",        0,4536,   0, None,         "Pumpkin",      None,     "Flour",     None,           35),
    ("Orcrest Garlic Apple Jelly",               5,1,10, "Fruit",        0,4536,   0, None,         "Apples",       None,     "Garlic",    None,           35),
    ("Ordinator's Beetle-Cheese Soup",           5,1,10, "Fruit",        0,4536,   0, None,         "Tomato",       None,     "Cheese",    None,           35),
    ("Baby Carrots in Moon-Sugar Glaze",         5,1,10, "Vegetable",    0,   0,4536, None,         None,           "Carrots","Seasoning", None,           35),
    ("Velothi Cabbage Soup",                     5,1,10, "Vegetable",    0,   0,4536, None,         None,           "Greens", "Saltrice",  None,           35),
    ("West Weald Corn Chowder",                  5,1,10, "Vegetable",    0,   0,4536, None,         None,           "Corn",   "Millet",    None,           35),
    ("Ashlander Nix-Hound Chili",                5,2,10, "Savoury",  4079,3732,   0, "White Meat", "Pumpkin",      None,     "Garlic",    None,           60),
    ("Colovian Beef Noodle Soup",                5,2,10, "Savoury",  4079,3732,   0, "Red Meat",   "Tomato",       None,     "Flour",     None,           60),
    ("Seared Slaughterfish with Mammoth Cheese", 5,2,10, "Savoury",  4079,3732,   0, "Fish",       "Jazbay Grapes",None,     "Cheese",    None,           60),
    ("Goblin-Style Grilled Rat",                 5,2,10, "Ragout",   4079,   0,3732, "Small Game", None,           "Beets",  "Seasoning", None,           60),
    ("Grilled Camel on Cornbread",               5,2,10, "Ragout",   4079,   0,3732, "Game",       None,           "Corn",   "Millet",    None,           60),
    ("Potato-Stuffed Roast Pheasant",            5,2,10, "Ragout",   4079,   0,3732, "Poultry",    None,           "Potato", "Saltrice",  None,           60),
    ("Eidar Banana-Radish Vichyssoise",          5,2,10, "Entremet",    0,3732,3732, None,         "Bananas",      "Radish", "Cheese",    None,           60),
    ("Khajiiti Apple Spanakopita",               5,2,10, "Entremet",    0,3732,3732, None,         "Apples",       "Greens", "Flour",     None,           60),
    ("Savory Mid Year Preserves",                5,2,10, "Entremet",    0,3732,3732, None,         "Melon",        "Carrots","Garlic",    None,           60),
    ("Braised Sweetmeats",                       5,3,10, "Gourmet",  3412,3139,3139, "Red Meat",   "Bananas",      "Radish", None,"Frost Mirriam",        120),
    ("Goatherd's Pie",                           5,3,10, "Gourmet",  3412,3139,3139, "Game",       "Melon",        "Beets",  None,"Frost Mirriam",        120),
    ("Planked Abecean Longfin",                  5,3,10, "Gourmet",  3412,3139,3139, "Fish",       "Apples",       "Beets",  None,"Frost Mirriam",        120),
    ("Slow-Simmered Rabbit Goulash",             5,3,10, "Gourmet",  3412,3139,3139, "Small Game", "Tomato",       "Carrots",None,"Frost Mirriam",        120),

    # ── Level 100, RI 6, RQ 1 ────────────────────────────────────────────────
    ("Crawdad Quiche",                   6,1,100,"Meat",      6195,   0,   0, "Fish",       None,           None,     "Millet",    None,           35),
    ("Orcish Bratwurst on Bun",          6,1,100,"Meat",      6195,   0,   0, "White Meat", None,           None,     "Flour",     None,           35),
    ("The Skald-King's Patty Melt",      6,1,100,"Meat",      6195,   0,   0, "Red Meat",   None,           None,     "Cheese",    None,           35),
    ("Bananas in Moon-Sugar Syrup",      6,1,100,"Fruit",        0,5670,   0, None,         "Bananas",      None,     "Seasoning", None,           35),
    ("Garlic Guar Stuffed Grape Leaves", 6,1,100,"Fruit",        0,5670,   0, None,         "Jazbay Grapes",None,     "Garlic",    None,           35),
    ("House Hlaalu Pumpkin Risotto",     6,1,100,"Fruit",        0,5670,   0, None,         "Pumpkin",      None,     "Saltrice",  None,           35),
    ("Nord Warrior Potato Porridge",     6,1,100,"Vegetable",    0,   0,5670, None,         None,           "Potato", "Millet",    None,           35),
    ("Taneth Chili Cheese Corn",         6,1,100,"Vegetable",    0,   0,5670, None,         None,           "Corn",   "Cheese",    None,           35),
    ("The Secret Chef's Beet Crostata",  6,1,100,"Vegetable",    0,   0,5670, None,         None,           "Beets",  "Flour",     None,           35),

    # ── Level 100, RI 6, RQ 2 ────────────────────────────────────────────────
    ("Coldharbour Daedrat Snacks",       6,2,100,"Savoury",  5066,4635,   0, "Small Game", "Apples",       None,     "Garlic",    None,           60),
    ("Lillandril Summer Sausage",        6,2,100,"Savoury",  5066,4635,   0, "White Meat", "Melon",        None,     "Seasoning", None,           60),
    ("Sweet Horker Stew",                6,2,100,"Savoury",  5066,4635,   0, "Red Meat",   "Jazbay Grapes",None,     "Saltrice",  None,           60),
    ("Breton Bubble-and-Squeak",         6,2,100,"Ragout",   5066,   0,4635, "Game",       None,           "Greens", "Flour",     None,           60),
    ("Kwama Egg Omelet",                 6,2,100,"Ragout",   5066,   0,4635, "Poultry",    None,           "Carrots","Cheese",    None,           60),
    ("Silverside Perch Pudding",         6,2,100,"Ragout",   5066,   0,4635, "Fish",       None,           "Beets",  "Millet",    None,           60),
    ("Arenthia's Empty Tankard Frittata",6,2,100,"Entremet",    0,4635,4635, None,         "Tomato",       "Potato", "Garlic",    None,           60),
    ("Boiled Creme Treat",               6,2,100,"Entremet",    0,4635,4635, None,         "Pumpkin",      "Radish", "Saltrice",  None,           60),
    ("Sweetroll",                        6,2,100,"Entremet",    0,4635,4635, None,         "Bananas",      "Corn",   "Seasoning", None,           60),

    # ── Level 100, RI 6, RQ 3 (Gourmet) ─────────────────────────────────────
    ("Potentate's Supreme Cioppino",     6,3,100,"Gourmet", 4200,3864,3864, "Fish",       "Pumpkin",      "Corn",   None,"Frost Mirriam",          120),
    ("The Emperor's Venison Fricassee",  6,3,100,"Gourmet", 4200,3864,3864, "Game",       "Melon",        "Carrots",None,"Frost Mirriam",          120),
    ("The Secret Chef's Pork Roast",     6,3,100,"Gourmet", 4200,3864,3864, "White Meat", "Jazbay Grapes","Potato", None,"Frost Mirriam",          120),
    ("Ultimate Riverhold Beef Pasty",    6,3,100,"Gourmet", 4200,3864,3864, "Red Meat",   "Tomato",       "Radish", None,"Frost Mirriam",          120),

    # ── Level 150, RI 6, RQ 1 ────────────────────────────────────────────────
    ("Garlic-and-Pepper Venison Steak",  6,1,150,"Meat",      6608,   0,   0, "Game",       None,           None,     "Garlic",    None,           35),
    ("Lilmoth Garlic Hagfish",           6,1,150,"Meat",      6608,   0,   0, "Fish",       None,           None,     "Garlic",    None,           35),
    ("Millet and Beef Stuffed Peppers",  6,1,150,"Meat",      6608,   0,   0, "Red Meat",   None,           None,     "Millet",    None,           35),
    ("Firsthold Fruit and Cheese Plate", 6,1,150,"Fruit",        0,6048,   0, None,         "Jazbay Grapes",None,     "Cheese",    None,           35),
    ("Thrice-Baked Gorapple Pie",        6,1,150,"Fruit",        0,6048,   0, None,         "Apples",       None,     "Saltrice",  None,           35),
    ("Tomato Garlic Chutney",            6,1,150,"Fruit",        0,6048,   0, None,         "Tomato",       None,     "Garlic",    None,           35),
    ("Bravil's Best Beet Risotto",       6,1,150,"Vegetable",    0,   0,6048, None,         None,           "Beets",  "Saltrice",  None,           35),
    ("Hearty Garlic Corn Chowder",       6,1,150,"Vegetable",    0,   0,6048, None,         None,           "Corn",   "Garlic",    None,           35),
    ("Tenmar Millet-Carrot Couscous",    6,1,150,"Vegetable",    0,   0,6048, None,         None,           "Carrots","Millet",    None,           35),

    # ── Level 150, RI 6, RQ 2 ────────────────────────────────────────────────
    ("Melon-Baked Parmesan Pork",            6,2,150,"Savoury",  5395,4936,   0, "White Meat", "Melon",        None,     "Cheese",    None,           60),
    ("Mistral Banana-Bunny Hash",            6,2,150,"Savoury",  5395,4936,   0, "Small Game", "Bananas",      None,     "Seasoning", None,           60),
    ("Solitude Salmon-Millet Soup",          6,2,150,"Savoury",  5395,4936,   0, "Fish",       "Tomato",       None,     "Millet",    None,           60),
    ("Braised Rabbit with Spring Vegetables",6,2,150,"Ragout",   5395,   0,4936, "Small Game", None,           "Greens", "Seasoning", None,           60),
    ("Garlic Cod with Potato Crust",         6,2,150,"Ragout",   5395,   0,4936, "Fish",       None,           "Potato", "Garlic",    None,           60),
    ("Sticky Pork and Radish Noodles",       6,2,150,"Ragout",   5395,   0,4936, "White Meat", None,           "Radish", "Flour",     None,           60),
    ("Chevre-Radish Salad with Pumpkin Seeds",6,2,150,"Entremet",   0,4936,4936, None,        "Pumpkin",      "Radish", "Cheese",    None,           60),
    ("Grapes and Ash Yam Falafel",           6,2,150,"Entremet",    0,4936,4936, None,         "Jazbay Grapes","Potato", "Millet",    None,           60),
    ("Late Hearthfire Vegetable Tart",       6,2,150,"Entremet",    0,4936,4936, None,         "Pumpkin",      "Beets",  "Flour",     None,           60),

    # ── Level 150, RI 6, RQ 3 (Gourmet) ─────────────────────────────────────
    ("Capon Tomato-Beet Casserole",          6,3,150,"Gourmet", 4462,4105,4105, "Poultry",    "Tomato",       "Beets",  None,"Frost Mirriam",         120),
    ("Jugged Rabbit in Preserves",           6,3,150,"Gourmet", 4462,4105,4105, "Small Game", "Bananas",      "Carrots",None,"Frost Mirriam",         120),
    ("Longfin Pasty with Melon Sauce",       6,3,150,"Gourmet", 4462,4105,4105, "Fish",       "Melon",        "Greens", None,"Frost Mirriam",         120),
    ("Withered Tree Inn Venison Pot Roast",  6,3,150,"Gourmet", 4462,4105,4105, "Game",       "Apples",       "Carrots",None,"Frost Mirriam",         120),

    # ── Special / Event Food & Drink (festival rewards, scales to player level) ─
    # Stat columns reflect max-stat bonuses only; recovery bonuses not captured.
    ("Aetherial Ambrosia",                      6,4,1,"Special",   0,   0,   0, "Psijic Ambrosia",       "Diminished Aetherial Dust",None,                 None,                     None,           30),
    ("Alcaire Festival Sword-Pie",              1,1,1,"Special",6160,   0,   0, "Red Meat",              "Seasoning",              "Flour",               None,                     None,          120),
    ("Artaeum Pickled Fish Bowl",               6,3,1,"Special",5414,4938,   0, "Fish",                  "Rice",                   "Clam Gall",           "Honey",                  None,          120),
    ("Artaeum Takeaway Broth",                  6,4,1,"Special",3326,   0,3080, "Fish",                  "Melon",                  "Torchbug Thorax",     "Powdered Mother of Pearl",None,         120),
    ("Bergama Warning Fire",                    2,2,1,"Special",   0,   0,4936, "Coffee",                "Yerba Mate",             "Dragonthorn",         "Lotus",                  None,          120),
    ("Betnikh Twice-Spiked Ale",               2,2,1,"Special",   0,   0,   0, "Barley",                "Yeast",                  "Rice",                "Honey",                  None,          120),
    ('Bowl of "Peeled Eyeballs"',              2,2,1,"Special",   0,   0,   0, "Jazbay Grapes",         "Seasoning",              "Flour",               "Surilie Grapes",         None,          120),
    ("Bewitched Sugar Skulls",                  1,4,1,"Special",4620,4250,4250, "Scrib Jelly",           "Flour",                  "Columbine",           "Bervez Juice",           "Honey",       120),
    ("Candied Jester's Coins",                  1,2,1,"Special",   0,   0,4592, "Flour",                 "Coffee",                 "Imp Stool",           "Bervez Juice",           None,          120),
    ("Clockwork Citrus Filet",                  1,2,1,"Special",3326,3080,   0, "Red Meat",              "Lemon",                  "Frost Mirriam",       "Perfect Roe",            None,          120),
    ("Corrupting Bloody Mara",                  1,4,1,"Special",5051,4620,   0, "Nightshade",            "Daedra Heart",           "Dragon's Blood",      "Frost Mirriam",          None,          120),
    ("Crisp and Crunchy Pumpkin Snack Skewer",  1,2,1,"Special",   0,4592,4592, "Pumpkin",               "Potato",                 "Flour",               "Small Game",             None,          120),
    ("Crunchy Spider Skewer",                   1,2,1,"Special",   0,4592,   0, "Spider Egg",            "Crawlers",               "Acai Berry",          "Seasoning",              None,          120),
    ("Deregulated Mushroom Stew",               1,2,1,"Special",   0,   0,   0, "Namira's Rot",          "Small Game",             "Imp Stool",           None,                     None,          120),
    ("Dubious Camoran Throne",                  1,3,1,"Special",3094,   0,2856, "White Meat",            "Beetle Scuttle",         "Insect Parts",        "Guts",                   None,          120),
    ("Frosted Brains",                          1,2,1,"Special",   0,4592,   0, "White Meat",            "Honey",                  "Stinkhorn",           "Yeast",                  None,          120),
    ("Ghastly Eye Bowl",                        2,2,1,"Special",   0,4592,   0, "Worms",                 "Fleshfly Larva",         "Bananas",             "Rose",                   None,          120),
    ('Granny\'s Eel Pie',                       4,1,1,"Special",5790,   0,   0, "Yeast",                 "Flour",                  "Fish",                "Red Lichen",             None,          120),
    ("Hissmir Fish-Eye Rye",                    2,4,1,"Special",   0,   0,   0, "Fish",                  "Rye",                    "Corn Flower",         "Lemon",                  "Bervez Juice",120),
    ('Jagga-Drenched "Mud Ball"',               1,2,1,"Special",   0,4936,4936, "Coffee",                "Flour",                  "Seasoning",           "Cheese",                 None,          120),
    ("Jewels of Misrule",                       1,3,1,"Special",3927,   0,   0, "Rose",                  "Mint",                   "Lotus",               "Columbine",              "Bervez Juice",120),
    ("Lava Foot Soup-and-Saltrice",             1,2,1,"Special",   0,   0,4936, "Saltrice",              "Flour",                  "Potato",              "Scrib Jelly",            None,          120),
    ("Mythic Aetherial Ambrosia",               6,4,1,"Special",   0,   0,   0, "Psijic Ambrosia",       "Aetherial Dust",         None,                  None,                     None,           30),
    ("Old Aldmeri Orphan Gruel",                1,1,1,"Special",   0,5600,   0, "Barley",                "Rose",                   "Pumpkin",             None,                     None,          120),
    ("Orzorga's Blood Price Pie",               1,2,1,"Special",5395,   0,   0, "Red Meat",              "Potato",                 "Violet Coprinus",     "Guts",                   None,          120),
    ("Orzorga's Red Frothgar",                  2,2,1,"Special",5395,   0,   0, "Clear Water",           "Comberry",               "Honey",               "Mint",                   None,          120),
    ("Orzorga's Smoked Bear Haunch",            1,4,1,"Special",4312,   0,   0, "Red Meat",              "Tomato",                 "White Cap",           "Frost Mirriam",          "Perfect Roe", 120),
    ("Orzorga's Tripe Trifle Pocket",           1,2,1,"Special",5395,   0,   0, "Guts",                  "Columbine",              "Beets",               "White Meat",             None,          120),
    ("Pack Leader's Bone Broth",                1,4,1,"Special",5051,   0,4620, "Dragon Bone",           "Red Meat",               "Bone",                "Frost Mirriam",          None,          120),
    ("Princess's Delight",                      1,1,1,"Special",   0,5600,   0, "Flour",                 "Apples",                 "Butterfly Wing",      None,                     None,          120),
    ("Psijic Ambrosia",                         6,4,1,"Special",   0,   0,   0, "Perfect Roe",           "Frost Mirriam",          "Bervez Juice",        None,                     None,           30),
    ("Purifying Bloody Mara",                   2,4,1,"Special",5051,4620,   0, "Nirnroot",              "Tomato",                 "Daedra Heart",        "Frost Mirriam",          None,          120),
    ("Rajhin's Sugar Claws",                    1,1,1,"Special",   0,   0,5600, "Honey",                 "Corn",                   "Flour",               None,                     None,          120),
    ("Snow Bear Glow-Wine",                     2,1,1,"Special",   0,   0,   0, "Jazbay Grapes",         "Yeast",                  "Honey",               None,                     None,          120),
    ("Spring-Loaded Infusion",                  1,2,1,"Special",4165,3867,3867, "Dwarven Oil",           "Fish",                   "Bervez Juice",        "Water Hyacinth",         None,          120),
    ("Sweet Sanguine Apples",                   1,1,1,"Special",   0,5600,   0, "Apples",                "Honey",                  None,                  None,                     None,          120),
    ("Witchmother's Party Punch",               2,3,1,"Special",   0,   0,   0, "Bervez Juice",          "Rye",                    "Lotus",               "Lemon",                  None,          120),
    ("Witchmother's Potent Brew",               2,3,1,"Special",3094,2856,   0, "Nightshade",            "Bervez Juice",           "Rice",                "Small Game",             None,          120),
]

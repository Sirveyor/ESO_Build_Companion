lCREATE TABLE gear_items (
    id TEXT PRIMARY KEY,
    set_name TEXT NOT NULL,
    slot TEXT NOT NULL,
    weight TEXT,
    trait TEXT,
    quality TEXT,
    obtained INTEGER,
    stickerbook_unlocked INTEGER,
    location TEXT,
    source_notes TEXT,
    craftable INTEGER,
    transmute_cost INTEGER,
    notes TEXT,
    last_updated TEXT,
    custom_icon TEXT
);

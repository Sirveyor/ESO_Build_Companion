CREATE TABLE traits (
    id TEXT PRIMARY KEY,
    trait_type TEXT NOT NULL,
    research_status TEXT,
    research_end_time TEXT,
    craftable INTEGER,
    notes TEXT
);

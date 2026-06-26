CREATE TABLE builds (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    role TEXT NOT NULL,
    patch_version TEXT,
    source_link_id TEXT,
    notes TEXT,
    last_updated TEXT,
    favorite INTEGER,
    tags TEXT
);

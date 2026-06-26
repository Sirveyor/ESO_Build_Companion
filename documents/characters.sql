CREATE TABLE characters (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    race TEXT NOT NULL,
    role TEXT NOT NULL,
    level INTEGER NOT NULL,
    champion_points INTEGER NOT NULL,
    active_build_id TEXT,
    notes TEXT,
    last_updated TEXT,
    custom_portrait TEXT
);

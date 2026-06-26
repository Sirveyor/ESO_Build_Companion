CREATE TABLE skills (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    skill_line TEXT NOT NULL,
    morph TEXT,
    required_level INTEGER,
    obtained INTEGER,
    icon TEXT
);

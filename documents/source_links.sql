CREATE TABLE source_links (
    id TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    site_name TEXT,
    author TEXT,
    patch_version TEXT,
    last_checked TEXT,
    notes TEXT
);

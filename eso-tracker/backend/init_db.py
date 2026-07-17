# These imports register every model with Base.metadata so create_all() builds all tables.
from database import Base, engine
import models.user          # noqa: F401
import models.character     # noqa: F401
import models.build         # noqa: F401
import models.gear_set      # noqa: F401
import models.gear_item     # noqa: F401
import models.skill         # noqa: F401
import models.trait         # noqa: F401
import models.source_link   # noqa: F401
import models.links         # noqa: F401
import models.champion_points  # noqa: F401
import models.build_skills  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)
    _migrate()


def _migrate():
    """Safe incremental migrations for SQLite (ALTER TABLE ADD COLUMN is idempotent)."""
    from sqlalchemy import text
    migrations = [
        "ALTER TABLE traits ADD COLUMN character_id TEXT REFERENCES characters(id)",
        "ALTER TABLE characters ADD COLUMN alliance TEXT",
    ]
    with engine.connect() as conn:
        for sql in migrations:
            try:
                conn.execute(text(sql))
                conn.commit()
            except Exception:
                pass  # column already exists


if __name__ == "__main__":
    init_db()

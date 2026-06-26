from pathlib import Path
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()  # Load environment variables from .env file

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DB_PATH = BASE_DIR / "data" / "eso.db"
DB_PATH = Path(os.getenv("ESO_DB_PATH", str(DEFAULT_DB_PATH))).resolve()

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = F"sqlite:///{DB_PATH.as_posix()}"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

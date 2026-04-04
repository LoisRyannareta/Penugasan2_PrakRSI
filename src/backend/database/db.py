from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://mahasiswa-rsi:praktikum-rsi@localhost:5433/acara-rsi"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ini yang dipakai di router
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
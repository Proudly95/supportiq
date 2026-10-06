from collections.abc import Iterator

from sqlalchemy import Session, create_engine, sessionmaker

from app.core.orm import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


def get_db() -> Iterator[Session]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

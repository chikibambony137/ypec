from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

DATABASE_URL = config.DB_URL
engine = create_engine(DATABASE_URL)

def get_db():
    SessionLocal = sessionmaker(autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
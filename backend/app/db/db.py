from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
host = getenv("POSTGRES_HOST")
port = getenv("POSTGRES_PORT")
db = getenv("POSTGRES_DB")

# Create the database engine
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(DATABASE_URL)

# Create a base class for models
class Base(DeclarativeBase):
    pass

# Create a session local to the current thread
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    return SessionLocal()
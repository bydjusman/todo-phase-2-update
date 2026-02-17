from sqlmodel import create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")

# For SQLite, we need to use connect_args for proper foreign key support
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

# Create the engine
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.
    """
    with Session(engine) as session:
        yield session
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


# new connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(database_url, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

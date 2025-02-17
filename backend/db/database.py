from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Load database URL (modify with your actual credentials)
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/job_market_analytics"

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


# Dependency to get a session
async def get_db():
    async with SessionLocal() as session:
        yield session

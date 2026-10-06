from collections.abc import AsyncGenerator
from pathlib import Path
import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{Path(__file__).resolve().parents[2] / 'leadflow.db'}")
engine = create_async_engine(DATABASE_URL, future=True)
SessionFactory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session:
        yield session

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from src.config import Config

async_engine: AsyncEngine = create_async_engine(
    Config.DATABASE_URL, echo=True  # Optionally enable query logging
)


async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    # Create session factory bound to the async engine
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    # Use async context for the session
    async with Session() as session:
        yield session

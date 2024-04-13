from fastapi_storages import FileSystemStorage
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import DB_URL
from app.logger import logger


engine = create_async_engine(DB_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
logger.info(async_session_maker.configure)
storage = FileSystemStorage(path="static")


class Base(DeclarativeBase):
    pass



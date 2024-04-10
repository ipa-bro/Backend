from app.config import DB_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from fastapi_storages import FileSystemStorage



engine = create_async_engine(DB_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
storage = FileSystemStorage(path="/home/dimas/Backend/app/static")


class Base(DeclarativeBase):
    pass



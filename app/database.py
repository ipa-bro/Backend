from fastapi_storages import FileSystemStorage
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import DB_URL


engine = create_async_engine(
    url=DB_URL,
    pool_size=3,
    max_overflow=4
)
asession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
print(DB_URL)

storage = FileSystemStorage(path="static")


from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, String

from app.database import Base, storage


class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(FileType(storage=storage))
    title = Column(String, nullable=False)
    big_text = Column(String, nullable=False)
    small_text = Column(String, nullable=False)

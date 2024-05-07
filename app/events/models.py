from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, String

from app.database import Base, storage


class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photoUrl = Column(FileType(storage=storage), nullable=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    fullDescription = Column(String, nullable=False)

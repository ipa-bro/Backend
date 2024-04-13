from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, String

from app.database import Base, storage


class Members(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(FileType(storage=storage))
    fullname = Column(String, nullable=False)
    position = Column(String, nullable=False)
    date_of_birthday = Column(String, nullable=False)
    
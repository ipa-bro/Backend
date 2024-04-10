from app.database import Base, storage
from sqlalchemy import Column, Integer, String
from fastapi_storages.integrations.sqlalchemy import FileType


class Members(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(FileType(storage=storage))
    fullname = Column(String, nullable=False)
    position = Column(String, nullable=False)
    date_of_birthday = Column(String, nullable=False)
    
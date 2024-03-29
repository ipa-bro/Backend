from app.database import Base
from sqlalchemy import Column, Integer, String


class Members(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    type = Column(String, nullable=False)
    date_of_birthday = Column(String, nullable=False)
    text = Column(String, nullable=False)
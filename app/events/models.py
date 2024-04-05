from app.database import Base
from sqlalchemy import Column, Integer, String


class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String, nullable=False)
    title = Column(String, nullable=False)
    big_text = Column(String, nullable=False)
    small_text = Column(String, nullable=False)

from app.database import async_session_maker
from sqlalchemy import select


class BaseService:
    model = None

    @classmethod
    async def get_one_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id) 
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by) 
            result = await session.execute(query)
            return result.scalars().all()
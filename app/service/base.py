from sqlalchemy import select

from app.database import asession


class BaseService:
    """
    Базовый класс, который хранит 
    в себе методы: взять все записи 
    или взять запись по айди, далее при 
    наследовании подставляется модель
    """
    model = None

  
    @classmethod
    async def get_all(cls, **filter_by):
        async with asession() as session:
            query = select(cls.model).filter_by(**filter_by) 
            result = await session.execute(query)
            return result.scalars().all()
  

        
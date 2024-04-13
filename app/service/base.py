from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import logger


class BaseService:
    """
    Базовый класс, который хранит 
    в себе методы: взять все записи 
    или взять запись по айди, далее при 
    наследовании подставляется модель
    """
    model = None


    
    @classmethod
    async def get_one_by_id(cls, model_id: int):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(id=model_id) 
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database: Проблемы с базой"
            else:
                msg = "Other: Иные проблемы, проверьте код"
            logger.error(msg, exc_info=True)
            

    try:
        @classmethod
        async def get_all(cls, **filter_by):
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(**filter_by) 
                result = await session.execute(query)
                return result.scalars().all()
    except (SQLAlchemyError, Exception) as e:
        pass

        
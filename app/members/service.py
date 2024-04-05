from app.service.base import BaseService
from app.members.models import Members


class MembersService(BaseService):
    """
    Класс, который только подставляет модель
    Нужен для уровня абстракции
    """
    model = Members
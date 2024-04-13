from app.members.models import Members
from app.service.base import BaseService


class MembersService(BaseService):
    """
    Класс, который только подставляет модель
    Нужен для уровня абстракции
    """
    model = Members
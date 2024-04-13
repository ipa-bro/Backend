from app.events.models import Events
from app.service.base import BaseService


class EventsService(BaseService):
    """
    Класс, который только подставляет модель
    Нужен для уровня абстракции
    """
    model = Events
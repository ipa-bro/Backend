from app.service.base import BaseService
from app.events.models import Events


class EventsService(BaseService):
    """
    Класс, который только подставляет модель
    Нужен для уровня абстракции
    """
    model = Events
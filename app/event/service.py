from app.service.base import BaseService
from app.event.models import Events


class EventsService(BaseService):
    model = Events
from sqladmin import ModelView

from app.events.models import Events


class EventsAdmin(ModelView, model=Events):
    column_list = [c.name for c in Events.__table__.c]
    name = "Событие"
    name_plural = "События"
    icon = "fa-solid fa-location-dot"



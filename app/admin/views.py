from app.events.models import Events
from app.members.models import Members
from sqladmin import ModelView


class EventsAdmin(ModelView, model=Events):
    column_list = [c.name for c in Events.__table__.c]
    name = "Событие"
    name_plural = "События"
    icon = "fa-solid fa-location-dot"


class MembersAdmin(ModelView, model=Members):
    column_list = [c.name for c in Members.__table__.c]
    name = "Участник"
    name_plural = "Участники"
    icon = "fa-solid fa-user"
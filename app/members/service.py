from app.service.base import BaseService
from app.members.models import Members


class MembersService(BaseService):
    model = Members
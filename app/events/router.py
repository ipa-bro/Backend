from fastapi import APIRouter

from app.events.schemas import SEvents
from app.events.service import EventsService

router = APIRouter(
    prefix="/events",
    tags=["События"]
)


@router.get("")
async def get_events() -> list[SEvents]:
    result = await EventsService.get_all()
    return result


   
        
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.events.schemas import SEvents
from app.events.service import EventsService

router = APIRouter(
    prefix="/events",
    tags=["События"]
)


@router.get("")
@cache(expire=60)
async def get_events() -> list[SEvents]:
    result = await EventsService.get_all()
    return result


   
        
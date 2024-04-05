from app.events.service import EventsService
from app.events.schemas import SEvents, SEvent
from fastapi import APIRouter
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/event",
    tags=["События"]
)


@router.get("")
@cache(expire=60)
async def get_events() -> list[SEvents]:
    result = await EventsService.get_all()
    return result


@router.get("/{id}")
async def get_event(id: int) -> SEvent:
    result = await EventsService.get_one_by_id(id)
    return result
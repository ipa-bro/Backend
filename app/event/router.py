from app.event.service import EventsService
from app.event.schemas import SEvents
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
async def get_event(id: int) -> SEvents:
    result = await EventsService.get_one_by_id(id)
    return result
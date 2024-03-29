from app.event.service import EventsService
from fastapi import APIRouter


router = APIRouter(
    prefix="/event",
    tags=["События"]
)


@router.get("/")
async def get_events():
    result = await EventsService.get_all()
    return result
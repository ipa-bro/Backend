from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.members.schemas import SMembers
from app.members.service import MembersService

router = APIRouter(
    prefix="/members",
    tags=["Участники"]
)


@router.get("")
@cache(expire=60)
async def get_members() -> list[SMembers]:
    result = await MembersService.get_all()
    return result




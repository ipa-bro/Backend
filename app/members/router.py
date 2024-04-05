from app.members.service import MembersService
from app.members.schemas import SMembers
from fastapi import APIRouter
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/members",
    tags=["Участники"]
)


@router.get("")
@cache(expire=60)
async def get_members() -> list[SMembers]:
    result = await MembersService.get_all()
    return result




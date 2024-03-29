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


@router.get("/{id}")
async def get_members(id: int) -> SMembers:
    result = await MembersService.get_one_by_id(id)
    return result


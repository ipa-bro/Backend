from app.tasks.tasks import send_invite
import shutil
from fastapi import UploadFile
from fastapi import APIRouter


router = APIRouter(
    prefix="/invite",
    tags=["Заявка"]
)


@router.post("")
async def send_form(name: str, number: str, file: UploadFile):
    with open(f"app/static/{number}.png", "wb+") as image:
        shutil.copyfileobj(file.file, image)
    send_invite.delay(name, number)


import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import send_invite

router = APIRouter(
    prefix="/invite",
    tags=["Заявка"]
)


@router.post("")
async def send_form(name: str, number: str, file: UploadFile):
    with open(f"static/{number}.png", "wb+") as image:
            shutil.copyfileobj(file.file, image)
            send_invite.delay(name, number)
  
    


import shutil
from fastapi import UploadFile
from fastapi import APIRouter

#from app.tasks.tasks import mail



router = APIRouter(
    prefix="/invite",
    tags=["Заявка"]
)


@router.post("")
async def send_form(name: str, number: str, file: UploadFile):
    with open(f"app/static/{name}.webp", "wb+") as image:
        shutil.copyfileobj(file.file, image)
    invite_data = {"name": name, "number": number, "file": 12}
    #mail.delay(invite_data)


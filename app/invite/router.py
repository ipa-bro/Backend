import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form

from app.invite.tasks import send_invite

router = APIRouter(
    prefix="/invite",
    tags=["Заявка"]
)


@router.post("")
async def send_form(phone_number: str = Form(...), username: str = Form(...), pdf_file: UploadFile = File(...)):
    filename = f"{phone_number}.pdf"
    file_path = os.path.join("static", filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)
        send_invite(username, phone_number)
       

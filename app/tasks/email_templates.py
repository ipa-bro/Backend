from email.message import EmailMessage
from app.config import SMTP_USER, EMAIL_TO


def create_invite_message(data: dict):
    email = EmailMessage()
    email["Subjecct"] = "Новый участник"
    email["From"] = SMTP_USER
    email["To"] = EMAIL_TO
    email.set_content(
        f"""
            <h1>Новый участник</h1>
            ФИО: {data["name"]}
            Номер:{data["number"]}
            Фото
        """,
        subtype="html"
    )
from app.config import SMTP_USER, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def create_invite_message(name, number):
    msg = MIMEMultipart()
    msg['From'], msg['To'], msg['Subject'] = SMTP_USER, EMAIL_TO, "Новая заявка"
    msg.attach(MIMEText(f"""
            <h1>Новый участник</h1>
            ФИО: {name}
            </br>
            Номер: {number}
        """, "html"))
    file_path = f"app/static/{number}.png"
    with open(file_path, "rb") as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={file_path}")
    msg.attach(part)
    return msg
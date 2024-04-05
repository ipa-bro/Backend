from app.tasks.celery import celery
from app.tasks.email_templates import create_invite_message
from app.config import SMTP_HOST, SMTP_PASS, SMTP_PORT, SMTP_USER, EMAIL_TO
import smtplib


@celery.task
def send_invite(name: str, number: str):
    msg_content = create_invite_message(name, number)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.connect(SMTP_HOST, SMTP_PORT)
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, EMAIL_TO, msg_content.as_string())
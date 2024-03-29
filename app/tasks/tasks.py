from app.tasks.celery import celery
from app.tasks.email_templates import create_invite_message
from app.config import SMTP_HOST, SMTP_PASS, SMTP_PORT, SMTP_USER, EMAIL_TO
import smtplib


"""@celery.tasks
def mail(data: dict): #Доделать и сделать адекватную аннотацию
    msg_content= create_invite_message(data)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg_content)
"""

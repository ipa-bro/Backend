from app.config import REDIS_URL
from celery import Celery


celery = Celery(
    "tasks",
    broker=REDIS_URL,
    include=["app.tasks.tasks"]
)
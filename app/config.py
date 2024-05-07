import os

from dotenv import load_dotenv


load_dotenv()


POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
DB_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"


URL = "http://localhost:5173"


REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"


EMAIL_TO = os.getenv('EMAIL_TO')


SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASS = os.getenv('SMTP_PASS')


MODE = os.getenv('MODE')
LOG_LEVEL = os.getenv('LOG_LEVEL')


USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


SECRET_KEY = os.getenv('SECRET_KEY')

FROM python:3.10

COPY requirements.txt backend/requirements.txt

WORKDIR /backend

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN alembic upgrade head

CMD ["gunicorn" "app.main:app" "--workers 2" "--worker-class" "uvicorn.workers.UvicornWorker" "--bind=0.0.0.0:8000"]



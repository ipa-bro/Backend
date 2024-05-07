FROM python:3.10

COPY requirements.txt backend/requirements.txt

WORKDIR /backend

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod a+x /api/docker/*.sh


FROM python:3.10

COPY requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod a+x /api/docker/*.sh


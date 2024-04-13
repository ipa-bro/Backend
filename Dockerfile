FROM python:3.10

COPY requirements.txt /service/requirements.txt

WORKDIR /service

RUN pip install --upgrade pip && pip install -r requirements.txt && mkdir static

COPY . .

RUN chmod a+x /service/docker/*.sh


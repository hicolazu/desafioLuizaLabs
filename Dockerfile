FROM python:3.9.13-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./src /app

EXPOSE 8080

ENTRYPOINT exec python run.py

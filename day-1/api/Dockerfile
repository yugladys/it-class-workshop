FROM python:3.11-slim-bullseye 

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

CMD ["sh", "-c", "uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}"]

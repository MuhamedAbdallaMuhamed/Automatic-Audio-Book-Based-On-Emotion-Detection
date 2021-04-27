FROM python:3.8

WORKDIR /app

RUN apt -y update && apt install -y libsndfile1 && apt -y install espeak


COPY requirments.txt .
RUN pip3 install -r requirments.txt

COPY . .
ENV APP_DIRECTORY=/app
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:$PORT __init__:app
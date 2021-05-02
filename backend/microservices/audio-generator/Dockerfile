FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES=60
EXPOSE 5000
CMD gunicorn __init__:app


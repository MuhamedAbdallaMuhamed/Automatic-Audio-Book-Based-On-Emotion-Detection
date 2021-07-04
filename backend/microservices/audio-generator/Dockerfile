FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python -m spacy download en
RUN python commands.py
RUN git clone https://github.com/huggingface/neuralcoref.git &&\
    cd neuralcoref && pip install -r requirements.txt && pip install -e .

ENV JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES=60
EXPOSE 7000
CMD python __init__.py


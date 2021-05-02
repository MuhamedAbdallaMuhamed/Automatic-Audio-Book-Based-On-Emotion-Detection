FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN cd neuralcoref && pip install -r requirements.txt && pip install -e .\
    python -m spacy download en \
    python \
    import nltk \
    nltk.download('punkt') \
    nltk.download('averaged_perceptron_tagger') \
    nltk.download('maxent_ne_chunker') \
    nltk.download('words') \
    nltk.download('stopwords') \

COPY . .
ENV JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES=60
EXPOSE 3000
CMD python __init__.py


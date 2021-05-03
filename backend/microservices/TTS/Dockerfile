FROM python:3.8

WORKDIR /tts

RUN apt -y update && \
    apt install -y libsndfile1 && \
    apt -y install espeak
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

COPY ./requirements.txt /tts/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /tts
EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "/tts/main.py" ]

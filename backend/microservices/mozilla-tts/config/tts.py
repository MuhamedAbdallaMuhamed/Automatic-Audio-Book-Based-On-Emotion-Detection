import os

API_ROOT = 'https://bookbeat.herokuapp.com'

TOKEN_VALIDATION_ABS_ENDPOINT = API_ROOT + '/validate-token'

TTS_PORT = 5002
REQ_TTS_TEXT_KEY = 'text'
REQ_ACCESS_TOKEN_HEADER_NAME = 'Authorization'
REQ_REFRESH_TOKEN_HEADER_NAME = 'Authorization'

RES_TTS_MESSAGE_KEY = 'message'

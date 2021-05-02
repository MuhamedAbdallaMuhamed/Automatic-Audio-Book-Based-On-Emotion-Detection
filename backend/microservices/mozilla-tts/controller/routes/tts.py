from flask_restful import reqparse
from flask import send_file, request
import requests
import os
import sys

from . import api_bp
from config import *


tts_parser = reqparse.RequestParser()
tts_parser.add_argument(REQ_TTS_TEXT_KEY, type=str, required=True)

@api_bp.route('/tts', methods=('GET',))
def tts():
    tts_data = tts_parser.parse_args()
    # access_token = request.headers[REQ_ACCESS_TOKEN_HEADER_NAME]
    # r = requests.post(url=TOKEN_VALIDATION_ABS_ENDPOINT, headers={REQ_ACCESS_TOKEN_HEADER_NAME: access_token})
    # if '200' not in r.status_code:
    #     return {RES_TTS_MESSAGE_KEY: 'not authorized'}, 401

    text = tts_data[REQ_TTS_TEXT_KEY]
    stream = os.system(f'''tts --text="{text}" --model_name="tts_models/en/ljspeech/glow-tts" \
                --vocoder_name="vocoder_models/en/ljspeech/multiband-melgan"''')
    return send_file(
         f'{APP_PATH}/tts_output.wav',
         mimetype="audio/wav",
         as_attachment=True,
         attachment_filename="audio.wav")

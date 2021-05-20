from flask import request
from flask_restful import Resource, reqparse
from collections import deque
from werkzeug.utils import secure_filename
import requests
import os

from . import api
from config.routes import *
from core.usecases import *

tts_queue = deque()
cx_queue = deque()


def isInTtsQ(audio_order):
    for i in tts_queue:
        print(i)
        if i[0] == audio_order.id:
            return True
    return False


def isInCxQ(audio_order):
    for i in cx_queue:
        if i[0] == audio_order.id:
            return True
    return False


def get_order_status(audio_order):
    order = audio_order
    if order.cloned:
        if isInTtsQ(audio_order) or isInCxQ(audio_order):
            return RES_AUDIO_ORDER_WAITING_STATUS
        elif audio_order.audio_link is not None:
            return RES_AUDIO_ORDER_FINISHED_STATUS
        else:
            return RES_AUDIO_ORDER_GATH_STATUS
    else:
        if audio_order.audio_link is None:
            return RES_AUDIO_ORDER_WAITING_STATUS
        return RES_AUDIO_ORDER_FINISHED_STATUS


def to_orders_list(audio_orders: [AudioOrder]):
    orders_list = []
    for audio_order in audio_orders:
        orders_list.append({
            RES_AUDIO_ORDER_ID_KEY_NAME: audio_order.id,
            RES_AUDIO_ORDER_TITLE: audio_order.title,
            RES_AUDIO_ORDER_TEXT_KEY_NAME: [],
            RES_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME: audio_order.start_page,
            RES_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME: audio_order.end_page,
            RES_AUDIO_ORDER_STATUS: get_order_status(audio_order),
            RES_AUDIO_ORDER_AUDIO_LINK: audio_order.audio_link,
            RES_AUDIO_ORDER_AUDIO_CHARS: audio_order.chars_names,
            RES_AUDIO_ORDER_CLONED_KEY_NAME: audio_order.cloned,
        })
    return orders_list


def validate_user(access_token):
    r = requests.get(url=TOKEN_VALIDATION_ABS_ENDPOINT, headers={REQ_JSON_WEB_TOKEN_HEADER_NAME: str(access_token)})
    if 200 != r.status_code:
        raise Exception()

    return r.json()['id']


class AudioOrderResource(Resource):
    audio_order_post_parser = reqparse.RequestParser()
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_TITLE_KEY_NAME, type=str, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_TEXT_KEY_NAME, type=str, action="append", required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME, type=int, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME, type=int, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_CLONED_KEY_NAME, type=bool, required=True)
    audio_order_post_parser.add_argument(REQ_JSON_WEB_TOKEN_HEADER_NAME, required=True, location='headers')

    audio_order_put_parser = reqparse.RequestParser()
    audio_order_put_parser.add_argument(REQ_AUDIO_ORDER_ID_KEY_NAME, type=str, required=True, location='form')
    audio_order_put_parser.add_argument(REQ_JSON_WEB_TOKEN_HEADER_NAME, required=True, location='headers')

    audio_order_get_parser = reqparse.RequestParser()
    audio_order_get_parser.add_argument(REQ_JSON_WEB_TOKEN_HEADER_NAME, required=True, location='headers')

    def get(self):
        access_token = self.audio_order_get_parser.parse_args()[REQ_JSON_WEB_TOKEN_HEADER_NAME]
        try:
            user_id = validate_user(access_token)
        except():
            return {RES_MESSAGE_KEY_NAME: 'access token is invalid'}, 400

        audio_orders = get_audio_orders(user_id)
        return {
                   RES_MESSAGE_KEY_NAME: 'Your orders',
                   RES_AUDIO_ORDER_ORDERS: to_orders_list(audio_orders)
               }, 200

    def post(self):
        audio_order_req = self.audio_order_post_parser.parse_args()
        access_token = audio_order_req[REQ_JSON_WEB_TOKEN_HEADER_NAME]
        try:
            user_id = validate_user(access_token)
        except():
            return {RES_MESSAGE_KEY_NAME: 'access token is invalid'}, 400
        audio_order = add_audio_order(
            user_id=user_id,
            title=audio_order_req[REQ_AUDIO_ORDER_TITLE_KEY_NAME],
            text=audio_order_req[REQ_AUDIO_ORDER_TEXT_KEY_NAME],
            start_page=audio_order_req[REQ_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME],
            end_page=audio_order_req[REQ_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME],
            cloned=audio_order_req[REQ_AUDIO_ORDER_CLONED_KEY_NAME]
        )
        if audio_order.cloned:
            cx_queue.append((audio_order.id, audio_order.text))
        else:
            tts_queue.append((audio_order.id, None, None, audio_order.text))  # scripts, chars_audio, list_pargraphes
        return {RES_MESSAGE_KEY_NAME: 'Your request has been recorded'}, 200

    def put(self):
        req = self.audio_order_put_parser.parse_args()
        access_token = req[REQ_JSON_WEB_TOKEN_HEADER_NAME]
        try:
            validate_user(access_token)
        except():
            return {RES_MESSAGE_KEY_NAME: 'access token is invalid'}, 400
        id = req[REQ_AUDIO_ORDER_ID_KEY_NAME]
        update_audio_order(audio_link=None, chars_names=None, id=id, scripts=None)
        chars = {}
        for char_name in request.files:
            print(char_name)
            file_name = secure_filename(str(id) + char_name + request.files[char_name].filename)
            request.files[char_name].save(file_name)
            pre, ext = os.path.splitext(file_name)
            os.rename(file_name, pre + '.ogg')
            chars[char_name] = pre + '.ogg'
        audio_order = get_audio_order(id)
        tts_queue.append((id, audio_order.scripts, chars, audio_order.text))  # scripts, chars_names, senteces
        return {RES_MESSAGE_KEY_NAME: "Your request will be processed"}, 200,  # bad reques


api.add_resource(AudioOrderResource, AUDIO_ORDER_ABS_ENDPOINT_NAME)

######
from .queue_handlers import QueuesHandlers

QueuesHandlers.run_queue_handlers()
# thread
#####

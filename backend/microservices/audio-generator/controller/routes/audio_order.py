from flask import request
from flask_restful import Resource, reqparse
from collections import deque
from werkzeug.utils import secure_filename

from config import AUTHOR_NAME
from .helpers import valid_access_token
import os
from . import api
from config.routes import *
from core.usecases import *

tts_queue = deque()
cx_queue = deque()


def is_in_tts_q(audio_order):
    for i in tts_queue:
        if i[0] == audio_order.id:
            return True
    return False


def is_in_cx_q(audio_order):
    for i in cx_queue:
        if i[0] == audio_order.id:
            return True
    return False


def get_order_status(audio_order):
    if is_in_tts_q(audio_order) or is_in_cx_q(audio_order):
        return RES_AUDIO_ORDER_WAITING_STATUS
    elif audio_order.audio_link is not None:
        return RES_AUDIO_ORDER_FINISHED_STATUS
    else:
        return RES_AUDIO_ORDER_GATH_STATUS


def to_orders_list(audio_orders: [AudioOrder]):
    orders_list = []
    for audio_order in audio_orders:
        orders_list.append({
            RES_AUDIO_ORDER_ID_KEY_NAME: audio_order.id,
            RES_AUDIO_ORDER_TITLE: audio_order.title,
            RES_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME: audio_order.start_page,
            RES_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME: audio_order.end_page,
            RES_AUDIO_ORDER_STATUS: get_order_status(audio_order),
            RES_AUDIO_ORDER_AUDIO_LINK: audio_order.audio_link,
            RES_AUDIO_ORDER_AUDIO_CHARS: audio_order.chars_names,
            RES_AUDIO_ORDER_CLONED_KEY_NAME: audio_order.cloned,
        })
    return orders_list


class AudioOrderResource(Resource):
    audio_order_post_parser = reqparse.RequestParser()
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_TITLE_KEY_NAME, type=str, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME, type=int, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME, type=int, required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_TEXT_KEY_NAME, type=str, action='append', required=True)
    audio_order_post_parser.add_argument(REQ_AUDIO_ORDER_CLONED_KEY_NAME, type=bool, required=True)

    audio_order_put_parser = reqparse.RequestParser()
    audio_order_put_parser.add_argument(REQ_AUDIO_ORDER_ID_KEY_NAME, type=str, required=True, location='form')

    audio_order_get_parser = reqparse.RequestParser()
    audio_order_get_parser.add_argument(REQ_USER_ID_KEY_NAME, type=str, required=True)

    @valid_access_token
    def get(self):
        user_id = self.audio_order_get_parser.parse_args()[REQ_USER_ID_KEY_NAME]
        audio_orders = get_audio_orders(user_id)
        return {
                   RES_MESSAGE_KEY_NAME: 'Your orders',
                   RES_AUDIO_ORDER_ORDERS: to_orders_list(audio_orders)
               }, 200

    @valid_access_token
    def post(self):
        audio_order_req = self.audio_order_post_parser.parse_args()
        audio_order = add_audio_order(
            user_id=request.args.get(REQ_USER_ID_KEY_NAME),
            title=audio_order_req[REQ_AUDIO_ORDER_TITLE_KEY_NAME],
            text=audio_order_req[REQ_AUDIO_ORDER_TEXT_KEY_NAME],
            start_page=audio_order_req[REQ_AUDIO_ORDER_STARTING_PAGE_NUMBER_KEY_NAME],
            end_page=audio_order_req[REQ_AUDIO_ORDER_ENDING_PAGE_NUMBER_KEY_NAME],
            cloned=audio_order_req[REQ_AUDIO_ORDER_CLONED_KEY_NAME],
        )
        if audio_order.cloned == 1:
            cx_queue.append((audio_order.id, audio_order.text, False))
        elif audio_order.cloned == 2:
            cx_queue.append((audio_order.id, audio_order.text, True))
        else:
            tts_queue.append((audio_order.id, None, False))  # scripts, chars_audio, list_pargraphes
        return {RES_MESSAGE_KEY_NAME: 'Your request has been recorded'}, 200

    @valid_access_token
    def put(self):
        req = self.audio_order_put_parser.parse_args()
        id = req[REQ_AUDIO_ORDER_ID_KEY_NAME]
        update_audio_order(audio_link=None, chars_names=None, id=id, scripts=None)
        chars = {}
        has_author = False
        for char_name in request.files:
            file_name = secure_filename(str(id) + char_name + request.files[char_name].filename)
            request.files[char_name].save(file_name)
            pre, ext = os.path.splitext(file_name)
            has_author = (char_name == AUTHOR_NAME)
            os.rename(file_name, pre + '.ogg')
            chars[char_name] = pre + '.ogg'

        tts_queue.append((id, chars, has_author))  # scripts, chars_names, senteces
        return {RES_MESSAGE_KEY_NAME: "Your request will be processed"}, 200,  # bad reques


api.add_resource(AudioOrderResource, AUDIO_ORDER_ABS_ENDPOINT_NAME)

from .queue_handlers import QueuesHandlers
QueuesHandlers.run_queue_handlers()



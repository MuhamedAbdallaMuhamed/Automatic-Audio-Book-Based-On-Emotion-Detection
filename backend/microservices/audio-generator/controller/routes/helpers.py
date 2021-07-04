from flask import request
from flask_restful import reqparse
from config import REQ_JSON_WEB_TOKEN_HEADER_NAME, TOKEN_VALIDATION_ABS_ENDPOINT, RES_MESSAGE_KEY_NAME
from werkzeug.datastructures import ImmutableMultiDict
from functools import wraps
import requests

auth = reqparse.RequestParser()
auth.add_argument(REQ_JSON_WEB_TOKEN_HEADER_NAME, required=True, location='headers')


def valid_access_token(func):
    @wraps(func)
    def validate_user(*args, **kwargs):
        access_token = auth.parse_args()[REQ_JSON_WEB_TOKEN_HEADER_NAME]
        r = requests.get(url=TOKEN_VALIDATION_ABS_ENDPOINT,
                         headers={REQ_JSON_WEB_TOKEN_HEADER_NAME: str(access_token)})
        if r.status_code != 200:
            return {RES_MESSAGE_KEY_NAME: 'access token is invalid'}, 400

        args_dict = request.args.to_dict()
        args_dict['id'] = r.json()['id']
        request.args = ImmutableMultiDict(args_dict)
        return func(*args, **kwargs)
    return validate_user

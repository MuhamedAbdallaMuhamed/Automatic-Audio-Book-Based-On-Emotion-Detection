import os

from flask import request
from flask_restful import reqparse
from config import REQ_JSON_WEB_TOKEN_HEADER_NAME, TOKEN_VALIDATION_ABS_ENDPOINT, RES_MESSAGE_KEY_NAME
from werkzeug.datastructures import ImmutableMultiDict
from functools import wraps
import requests
import fitz

auth = reqparse.RequestParser()
auth.add_argument(REQ_JSON_WEB_TOKEN_HEADER_NAME, required=True, location='headers')


def valid_access_token(func):
    @wraps(func)
    def validate_user(*args, **kwargs):
        access_token = auth.parse_args()[REQ_JSON_WEB_TOKEN_HEADER_NAME]
        r = requests.get(url=TOKEN_VALIDATION_ABS_ENDPOINT,
                         headers={REQ_JSON_WEB_TOKEN_HEADER_NAME: str(access_token)})
        if 200 != r.status_code:
            return {RES_MESSAGE_KEY_NAME: 'access token is invalid'}, 400

        args_dict = request.args.to_dict()
        args_dict['id'] = r.json()['id']
        request.args = ImmutableMultiDict(args_dict)
        return func(*args, **kwargs)
    return validate_user


def pdf_to_text_list(file, start_page, end_page):
    file.save('temp_pdf.pdf')
    text_list = []
    i = 1
    with fitz.open("temp_pdf.pdf") as doc:
        for page in doc:
            if start_page <= i <= end_page:
                text_list.append(page.getText())
            elif i > end_page:
                break
            i += 1
    os.remove("temp_pdf.pdf")
    return text_list
from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from datetime import timedelta

from . import api
from config import *
from core.entities import hash_password
from core.usecases import get_user


class LoginResource(Resource):
    login_parser = reqparse.RequestParser()
    login_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=True)
    login_parser.add_argument(REQ_USER_PASSWORD_KEY_NAME, type=str, required=True)

    def post(self):
        # parsing the coming request
        login_data = LoginResource.login_parser.parse_args()

        email = login_data[REQ_USER_EMAIL_KEY_NAME]
        user = get_user(email=email)
        if user:
            password = login_data[REQ_USER_PASSWORD_KEY_NAME]
            if hash_password(password, user.salt) == user.hashed_password:
                # creating access token
                expires = timedelta(minutes=JWT_ACCESS_TOKEN_LIFETIME)
                access_token = create_access_token(user.id, expires=expires, fresh=True)
                # creating refresh token
                expires = timedelta(minutes=JWT_REFRESH_TOKEN_LIFETIME)
                refresh_token = create_refresh_token(user.id, expires=expires)
                # user logged-in successfully
                return {
                    RES_MESSAGE_KEY_NAME: 'Logged in',
                    RES_ACCESS_TOKEN_KEY_NAME: access_token,
                    RES_REFRESH_TOKEN_KEY_NAME: refresh_token
                }
        # wrong email or password
        return {
            'status': 401,  # HTTP unauthorized client error
            RES_MESSAGE_KEY_NAME: 'bad credentials'
        }


api.add_resource(LoginResource, LOGIN_ABS_ENDPOINT_NAME)

from flask_restful import reqparse, Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

from . import api
from config import *
from core.entities import hash_password
from core.usecases import get_user


class LoginResource(Resource):
    login_parser = reqparse.RequestParser()
    login_parser.add_argument(LOGIN_EMAIL_KEY_NAME, required=True)
    login_parser.add_argument(LOGIN_PASSWORD_KEY_NAME, required=True)

    def post(self):
        # parsing the coming request
        login_data = LoginResource.login_parser.parse_args()

        email = login_data[LOGIN_EMAIL_KEY_NAME]
        user = get_user(email=email)
        if user:
            password = login_data[LOGIN_PASSWORD_KEY_NAME]
            if hash_password(password, user.salt) == user.hashed_password:
                # creating access token
                expires = timedelta(minutes=ACCESS_TOKEN_LIFETIME)
                access_token = create_access_token(user.email, expires_delta=expires)
                # creating refresh token
                expires = timedelta(minutes=REFRESH_TOKEN_LIFETIME)
                refresh_token = create_refresh_token(user.email, expires_delta=expires)
                # user logged-in successfully
                return {
                    MESSAGE_HEADER_NAME: 'Logged in',
                    ACCESS_TOKEN_HEADER_NAME: access_token,
                    REFRESH_TOKEN_HEADER_NAME: refresh_token
                }
        # wrong email or password
        return {
            'status': 401,  # HTTP unauthorized client error
            MESSAGE_HEADER_NAME: 'bad credentials'
        }


api.add_resource(LoginResource, LOGIN_ABS_ENDPOINT_NAME)

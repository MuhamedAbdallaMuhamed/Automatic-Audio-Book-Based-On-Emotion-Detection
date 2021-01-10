from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from datetime import timedelta

from . import api
from config import *
from core.entities import hash_password
from core.usecases import get_user


def valid_user_response(user):
    # creating access token
    expires = timedelta(minutes=ACCESS_TOKEN_LIFETIME)
    access_token = create_access_token(user.email, expires_delta=expires)
    # creating refresh token
    expires = timedelta(minutes=REFRESH_TOKEN_LIFETIME)
    refresh_token = create_refresh_token(user.email, expires_delta=expires)
    # user logged-in successfully
    return {
        MESSAGE_HEADER_NAME: 'Logged in',
        USER_FIRST_NAME_HEADER_NAME: user.first_name,
        USER_LAST_NAME_HEADER_NAME: user.last_name,
        USER_email_HEADER_NAME: user.email,
        USER_PROFILE_PICTURE_URL_HEADER_NAME: user.profile_picture_url,
        ACCESS_TOKEN_HEADER_NAME: access_token,
        REFRESH_TOKEN_HEADER_NAME: refresh_token,
    }


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
                return valid_user_response(user)
        # wrong email or password
        return {
            'status': 401,  # HTTP unauthorized client error
            MESSAGE_HEADER_NAME: 'bad credentials'
        }


class LoginByTokenResource(Resource):
    @jwt_required
    def post(self):
        user_email = get_jwt_identity()
        user = get_user(email=user_email)
        return valid_user_response(user)


api.add_resource(LoginResource, LOGIN_ABS_ENDPOINT_NAME)
api.add_resource(LoginByTokenResource, LOGIN_BY_TOKEN_ABS_ENDPOINT_NAME)


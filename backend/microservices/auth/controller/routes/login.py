from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from datetime import timedelta

from . import api
from config import *
from core.entities import hash_password
from core.usecases import get_user


def valid_user_response(user, generate_token):
    res = {
        RES_MESSAGE_KEY_NAME: 'Logged in',
        RES_USER_FIRST_NAME_KEY_NAME: user.first_name,
        RES_USER_LAST_NAME_KEY_NAME: user.last_name,
        RES_USER_EMAIL_KEY_NAME: user.email,
        RES_USER_PROFILE_PICTURE_URL_KEY_NAME: user.profile_picture_url
    }

    if generate_token:
        # creating access token
        expires = timedelta(minutes=JWT_ACCESS_TOKEN_LIFETIME)
        access_token = create_access_token(user.email, expires=expires, fresh=True)
        # creating refresh token
        expires = timedelta(minutes=JWT_REFRESH_TOKEN_LIFETIME)
        refresh_token = create_refresh_token(user.email, expires=expires)
        # user logged-in successfully
        res[RES_ACCESS_TOKEN_KEY_NAME] = access_token
        res[RES_REFRESH_TOKEN_NAME] = refresh_token

    return res


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
                return valid_user_response(user, generate_token=True)
        # wrong email or password
        return {
            'status': 401,  # HTTP unauthorized client error
            RES_MESSAGE_KEY_NAME: 'bad credentials'
        }


class LoginByTokenResource(Resource):
    @jwt_required
    def post(self):
        user_email = get_jwt_identity()
        user = get_user(email=user_email)
        return valid_user_response(user, generate_token=False)


api.add_resource(LoginResource, LOGIN_ABS_ENDPOINT_NAME)
api.add_resource(LoginByTokenResource, LOGIN_BY_TOKEN_ABS_ENDPOINT_NAME)

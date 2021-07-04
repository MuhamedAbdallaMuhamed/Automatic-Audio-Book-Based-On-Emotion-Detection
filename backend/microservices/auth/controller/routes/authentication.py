from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token, create_access_token

from . import app, api
from .user import auth_response
from config import *
from core.usecases import *
from google.oauth2 import id_token
from google.auth.transport import requests


class AuthenticationResource(Resource):
    authentication_parser = reqparse.RequestParser()
    authentication_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=True)
    authentication_parser.add_argument(REQ_GOOGLE_TOKEN_KEY_NAME, type=str, required=True)

    @staticmethod
    def post():
        # parsing the coming request
        authentication_data = AuthenticationResource.authentication_parser.parse_args()
        email = authentication_data[REQ_USER_EMAIL_KEY_NAME]
        token = authentication_data[REQ_GOOGLE_TOKEN_KEY_NAME]

        try:
            try:
                info = id_token.verify_oauth2_token(token, requests.Request())
                if info:
                    user = get_user_by_email(email=email)
                    if user == None:
                        return {RES_MESSAGE_KEY_NAME: "user is new for us."}, 400,  # not found
                    return auth_response(user), 200
                else:
                    return {RES_MESSAGE_KEY_NAME: "user token invalid."}, 401  # bad gate
            except ValueError:
                return {RES_MESSAGE_KEY_NAME: "user token invalid."}, 401,  # not found
        except Exception as e:
            app.logger.error(str(e))
            return {RES_MESSAGE_KEY_NAME: "an error has occurred"}, 404,  # bad reques


class ValidateTokenResource(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        return {RES_USER_ID_KEY_NAME: user_id}


api.add_resource(ValidateTokenResource, VALIDATE_TOKEN_ABS_ENDPOINT_NAME)
api.add_resource(AuthenticationResource, AUTHENTICATION_ABS_ENDPOINT_NAME)


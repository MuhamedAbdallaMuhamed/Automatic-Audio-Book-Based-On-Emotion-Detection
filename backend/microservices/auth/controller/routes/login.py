from flask_restful import reqparse, Resource
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity
from datetime import timedelta

from . import api, api_bp
from config import *
from core.entities import hash_password
from core.usecases import get_user
from .user import user_response


class LoginResource(Resource):
    login_parser = reqparse.RequestParser()
    login_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=False)
    login_parser.add_argument(REQ_USER_PASSWORD_KEY_NAME, type=str, required=False)

    def post(self):
        # parsing the coming request
        login_data = LoginResource.login_parser.parse_args()

        email = login_data[REQ_USER_EMAIL_KEY_NAME]
        user = get_user(email=email)
        if user:
            password = login_data[REQ_USER_PASSWORD_KEY_NAME]
            if hash_password(password, user.salt) == user.hashed_password:
                return user_response(user)
            else:  # wrong password
                return {RES_MESSAGE_KEY_NAME: 'Please check your password again'}, 401
        # wrong email
        return {RES_MESSAGE_KEY_NAME: '''The use doesn't exist'''}, 401  # HTTP unauthorized client error


@api_bp.route(REFRESH_TOKEN_ABS_ENDPOINT_NAME, methods=('POST',))
@jwt_refresh_token_required
def refresh_token():
    user_id = get_jwt_identity()
    user = get_user(id=user_id)
    if user:
        # creating access token
        expires = timedelta(minutes=JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES)
        access_token = create_access_token(user.id, expires_delta=expires, fresh=True)
        # user logged-in successfully
        return {
            RES_ACCESS_TOKEN_KEY_NAME: access_token,
        }
    # it's supposed to never reach this line of code
    return {RES_MESSAGE_KEY_NAME: 'bad credentials'}, 401  # HTTP unauthorized client error


api.add_resource(LoginResource, LOGIN_ABS_ENDPOINT_NAME)

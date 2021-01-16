from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import api
from .login import valid_user_response
from config import *
from core.usecases import *
from core.entities.exception import *


class UserResource(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument(REQ_USER_ID_KEY_NAME, type=str, jwt_required=False)
    user_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, jwt_required=False)
    user_parser.add_argument(REQ_USER_PASSWORD_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_FIRST_NAME_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_LAST_NAME_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_PHONE_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_GENDER_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_PROFILE_PICTURE_DATA_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_BIRTHDAY_KEY_NAME,
                             type=lambda x: datetime.strptime(x, REQ_USER_BIRTHDAY_FORMAT), required=False)

    @jwt_required
    def get(self):
        user_data = UserResource.user_parser.parse_args()
        if REQ_USER_ID_KEY_NAME in user_data:
            user = get_user(id=user_data[REQ_USER_ID_KEY_NAME])
        elif REQ_USER_EMAIL_KEY_NAME in user_data:
            user = get_user(email=user_data[REQ_USER_EMAIL_KEY_NAME])
        else:
            return {
                'status': 400,  # bad request
                RES_MESSAGE_KEY_NAME: 'user id or email is required'
            }
        return {
            RES_USER_ID_KEY_NAME: user.id,
            RES_USER_FIRST_NAME_KEY_NAME: user.first_name,
            RES_USER_LAST_NAME_KEY_NAME: user.last_name,
            RES_USER_EMAIL_KEY_NAME: user.email,
            RES_USER_PROFILE_PICTURE_URL_KEY_NAME: user.profile_picture_url
        }

    @jwt_required
    def post(self):
        user_data = UserResource.user_parser.parse_args()
        user_id = user_data[REQ_USER_ID_KEY_NAME]
        requested_user_id = get_jwt_identity()
        if user_id != requested_user_id:
            return {
                'status': 401,  # unauthorized
                RES_MESSAGE_KEY_NAME: 'you can only change your own data ;)'
            }

        first_name = user_data.get(REQ_USER_FIRST_NAME_KEY_NAME, None)
        last_name = user_data.get(REQ_USER_LAST_NAME_KEY_NAME, None)
        email = user_data.get(REQ_USER_EMAIL_KEY_NAME, None)
        password = user_data.get(REQ_USER_PASSWORD_KEY_NAME, None)
        phone = user_data.get(REQ_USER_PHONE_KEY_NAME, None)
        birthday = user_data.get(REQ_USER_BIRTHDAY_KEY_NAME, None)
        gender = user_data.get(REQ_USER_GENDER_KEY_NAME, None)
        profile_picture_data = user_data.get(REQ_USER_PROFILE_PICTURE_DATA_KEY_NAME, None)

        if update_user(
                id=user_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                phone=phone,
                birthday=birthday,
                gender=gender,
                profile_picture_data=profile_picture_data
        ):
            return {
                RES_MESSAGE_KEY_NAME: 'user has been updated successfully'
            }
        else:
            return {
                RES_MESSAGE_KEY_NAME: 'something went wrong'
            }


api.add_resource(UserResource, USER_ABS_ENDPOINT_NAME)

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required , get_raw_jwt

from . import api
from config import *
from core.usecases import *
from core.entities.exception import *


class RegisterResource(Resource):
    register_parser = reqparse.RequestParser()
    register_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_PASSWORD_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_FIRST_NAME_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_LAST_NAME_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_PHONE_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_GENDER_KEY_NAME, type=str, required=True)
    register_parser.add_argument(REQ_USER_BIRTHDAY_KEY_NAME,
                                 type=lambda x: datetime.strptime(x, REQ_USER_BIRTHDAY_FORMAT), required=True)
    register_parser.add_argument(REQ_USER_PROFILE_PICTURE_DATA_KEY_NAME, type=str, required=False)

    @jwt_required
    def post(self):
        # parsing the coming request
        register_data = RegisterResource.register_parser.parse_args()
        first_name = register_data[REQ_USER_FIRST_NAME_KEY_NAME]
        last_name = register_data[REQ_USER_LAST_NAME_KEY_NAME]
        email = register_data[REQ_USER_EMAIL_KEY_NAME]
        password = register_data[REQ_USER_PASSWORD_KEY_NAME]
        phone = register_data[REQ_USER_PHONE_KEY_NAME]
        birthday = register_data[REQ_USER_BIRTHDAY_KEY_NAME]
        gender = register_data[REQ_USER_GENDER_KEY_NAME]
        profile_picture_data = register_data.get(REQ_USER_PROFILE_PICTURE_DATA_KEY_NAME, None)

        try:
            add_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    gender=gender,
                    birthday=birthday,
                    profile_picture_data=profile_picture_data
                )
            return {
                'status': 201, # The request has been fulfilled, resulting in the creation of a new resource
                RES_MESSAGE_KEY_NAME: 'registered successfully'
            }
        except EmailException as e:
            return {
                'status': 400, # bad request
                RES_MESSAGE_KEY_NAME: str(e)
            }
        except PasswordException as e:
            return {
                'status': 400, # bad request
                RES_MESSAGE_KEY_NAME: str(e)
            }
        except PhoneException as e:
            return {
                'status': 400, # bad request
                RES_MESSAGE_KEY_NAME: str(e)
            }
        except NameException as e:
            return {
                'status': 400, # bad request
                RES_MESSAGE_KEY_NAME: str(e)
            }
        except Exception as e:
            return {
                'status': 400,  # bad request
                RES_MESSAGE_KEY_NAME: "an error has occurred"
            }


api.add_resource(RegisterResource, REGISTER_ABS_ENDPOINT_NAME)

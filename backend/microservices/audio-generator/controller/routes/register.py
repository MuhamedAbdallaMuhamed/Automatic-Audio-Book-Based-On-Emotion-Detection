from flask_restful import Resource, reqparse

from . import app, api
from .user import user_response
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

        try:
            add_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    gender=gender,
                    birthday=birthday,
                )
            user = get_user(email=email)
            # The request has been fulfilled, resulting in the creation of a new resource
            return user_response(user), 201
        except EmailException as e:
            return {RES_MESSAGE_KEY_NAME: str(e)}, 400,  # bad request
        except PasswordException as e:
            return {RES_MESSAGE_KEY_NAME: str(e)}, 400,  # bad request
        except PhoneException as e:
            return {RES_MESSAGE_KEY_NAME: str(e)}, 400,  # bad request
        except NameException as e:
            return {RES_MESSAGE_KEY_NAME: str(e)}, 400,  # bad request
        except Exception as e:
            app.logger.error(str(e))
            return {RES_MESSAGE_KEY_NAME: "an error has occurred"}, 400,  # bad reques


api.add_resource(RegisterResource, REGISTER_ABS_ENDPOINT_NAME)

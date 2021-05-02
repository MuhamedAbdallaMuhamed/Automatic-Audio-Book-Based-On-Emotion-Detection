from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token, create_access_token
from datetime import timedelta
from threading import Thread
from flask_mail import Message
from cryptography import fernet

from . import app, mail, api
from config import *
from core.usecases import *
from core.entities import send_email, generate_random_string_of_length
from core.entities.exception import *


def user_response(user):
    # creating access token
    expires = timedelta(minutes=JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES)
    access_token = create_access_token(user.id, expires_delta=expires, fresh=True)
    # creating refresh token
    expires = timedelta(minutes=JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES)
    refresh_token = create_refresh_token(user.id, expires_delta=expires)
    # user logged-in successfully
    return {
        RES_MESSAGE_KEY_NAME: 'Logged in',
        RES_ACCESS_TOKEN_KEY_NAME: access_token,
        RES_REFRESH_TOKEN_KEY_NAME: refresh_token,
        RES_USER_ID_KEY_NAME: user.id,
        RES_USER_FIRST_NAME_KEY_NAME: user.first_name,
        RES_USER_LAST_NAME_KEY_NAME: user.last_name,
        RES_USER_EMAIL_KEY_NAME: user.email,
        RES_USER_PROFILE_PICTURE_URL_KEY_NAME: user.profile_picture_url,
        RES_USER_BIRTHDAY_KEY_NAME: user.birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
        RES_USER_GENDER_KEY_NAME: user.gender,
        RES_USER_PHONE_KEY_NAME: user.phone
    }


def auth_response(user):
    # creating access token
    expires = timedelta(minutes=JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES)
    access_token = create_access_token(user.id, expires_delta=expires, fresh=True)
    # creating refresh token
    expires = timedelta(minutes=JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES)
    refresh_token = create_refresh_token(user.id, expires_delta=expires)
    # user logged-in successfully
    return {
        RES_MESSAGE_KEY_NAME: 'Logged in',
        RES_ACCESS_TOKEN_KEY_NAME: access_token,
        RES_REFRESH_TOKEN_KEY_NAME: refresh_token,
        RES_USER_ID_KEY_NAME: user.id,
        RES_USER_FIRST_NAME_KEY_NAME: user.first_name,
        RES_USER_LAST_NAME_KEY_NAME: user.last_name,
        RES_USER_EMAIL_KEY_NAME: user.email,
        RES_USER_PASSWORD_KEY_NAME: user.hashed_password,
        RES_USER_PROFILE_PICTURE_URL_KEY_NAME: user.profile_picture_url,
        RES_USER_BIRTHDAY_KEY_NAME: user.birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
        RES_USER_GENDER_KEY_NAME: user.gender,
        RES_USER_PHONE_KEY_NAME: user.phone
    }


class UserResource(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument(REQ_USER_ID_KEY_NAME, type=str, required=False)
    user_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=False)
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
        user_id = get_jwt_identity()
        user = get_user(id=user_id)
        return user_response(user)

    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        user_data = UserResource.user_parser.parse_args()
        first_name = user_data.get(REQ_USER_FIRST_NAME_KEY_NAME, None)
        last_name = user_data.get(REQ_USER_LAST_NAME_KEY_NAME, None)
        email = user_data.get(REQ_USER_EMAIL_KEY_NAME, None)
        password = user_data.get(REQ_USER_PASSWORD_KEY_NAME, None)
        phone = user_data.get(REQ_USER_PHONE_KEY_NAME, None)
        birthday = user_data.get(REQ_USER_BIRTHDAY_KEY_NAME, None)
        gender = user_data.get(REQ_USER_GENDER_KEY_NAME, None)
        profile_picture_data = user_data.get(REQ_USER_PROFILE_PICTURE_DATA_KEY_NAME, None)

        try:
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


class ForgetPasswordResource(Resource):
    forget_password_get_parser = reqparse.RequestParser()
    forget_password_get_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=True)

    forget_password_post_parser = reqparse.RequestParser()
    forget_password_post_parser.add_argument(REQ_USER_PASSWORD_RESET_CODE_KEY_NAME, type=str, required=True)
    forget_password_post_parser.add_argument(REQ_USER_EMAIL_KEY_NAME, type=str, required=True)
    forget_password_post_parser.add_argument(REQ_USER_PASSWORD_KEY_NAME, type=str, required=True)

    def get(self):
        forget_password_data = ForgetPasswordResource.forget_password_get_parser.parse_args()
        email = forget_password_data[REQ_USER_EMAIL_KEY_NAME]
        user = get_user(email=email)
        if user:
            reset_code = generate_random_string_of_length(16)
            update_user(user.id, reset_code=reset_code)
            msg = Message()
            msg.subject = "Reset Your Password Code"
            msg.recipients = [email]
            msg.body = reset_code
            msg.sender = SERVER_EMAIL_USERNAME
            Thread(target=send_email, args=(mail, app, msg)).start()
            return {
                RES_MESSAGE_KEY_NAME: 'A code sent to your email',
            }
        return {RES_MESSAGE_KEY_NAME: '''User doesn't exist'''}, 401  # HTTP unauthorized client error

    def put(self):
        forget_password_data = ForgetPasswordResource.forget_password_post_parser.parse_args()
        user = get_user(email=forget_password_data[REQ_USER_EMAIL_KEY_NAME])
        if not user:
            return {RES_MESSAGE_KEY_NAME: '''User doesn't exist'''}, 401

        reset_code = forget_password_data[REQ_USER_PASSWORD_RESET_CODE_KEY_NAME]
        if user.password_reset_code is None or user.password_reset_code != reset_code:
            return {RES_MESSAGE_KEY_NAME: 'Reset code is not correct'}, 401

        password = forget_password_data[REQ_USER_PASSWORD_KEY_NAME]
        try:
            if update_user(
                    id=user.id,
                    password=password
            ):
                return {
                    RES_MESSAGE_KEY_NAME: 'user has been updated successfully'
                }
            else:
                return {
                    RES_MESSAGE_KEY_NAME: 'something went wrong'
                }
        except PasswordException as e:
            return {RES_MESSAGE_KEY_NAME: str(e)}, 400,  # bad request
        except Exception as e:
            app.logger.error(str(e))
        return {RES_MESSAGE_KEY_NAME: "an error has occurred"}, 400,  # bad reques


api.add_resource(UserResource, USER_ABS_ENDPOINT_NAME)
api.add_resource(ForgetPasswordResource, FORGET_PASSWORD_ABS_ENDPOINT_NAME)

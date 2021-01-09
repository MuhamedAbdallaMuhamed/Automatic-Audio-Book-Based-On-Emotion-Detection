from .user import User
from .exception import *


def build_make_user(name_validator, email_validator, password_validator, phone_validator):
    def make_user(id, first_name, last_name, phone, email, password, profile_picture_url):
        # validate first_name
        if not name_validator(first_name):
            raise NameLengthLimitExceeded

        # validate last_name
        if not name_validator(last_name):
            raise NameLengthLimitExceeded

        # validate phone
        if not phone_validator(phone):
            raise PhoneNotValid

        # validate email
        if not email_validator(email):
            raise EmailNotValid

        # validate password
        if not password_validator(email):
            raise PasswordLengthLimitExceeded

        user = User(id, first_name, last_name, phone,
                    email, password, profile_picture_url)
        return user
    return make_user

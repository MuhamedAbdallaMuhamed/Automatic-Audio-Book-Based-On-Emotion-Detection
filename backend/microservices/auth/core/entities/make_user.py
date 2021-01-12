from .user import User
from .exception import *


def build_make_user(name_validator, email_validator, password_validator, phone_validator, hash_password, salt_generator):
    def make_user(id, first_name, last_name, phone, email, password, profile_picture_url, birthday, gender):
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

        salt = salt_generator()
        user = User(
                    id=id,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    hashed_password=hash_password(password, salt),
                    salt=salt,
                    profile_picture_url=profile_picture_url,
                    birthday=birthday,
                    gender=gender
                )
        return user
    return make_user

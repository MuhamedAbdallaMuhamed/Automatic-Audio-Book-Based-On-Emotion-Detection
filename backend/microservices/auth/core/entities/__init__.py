from .make_user import build_make_user
from .user import User


def email_validator(email: str):
    # validate email
    from ...config import USER_EMAIL_MAX_LENGTH
    if len(email) > USER_EMAIL_MAX_LENGTH:
        return False

    import re
    REGEX = '''^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'''
    if re.search(REGEX, email):
        return True

    return False


def password_validator(password: str):
    # validate password
    from ...config import USER_PASSWORD_MIN_LENGTH, USER_PASSWORD_MAX_LENGTH
    return USER_PASSWORD_MIN_LENGTH <= len(password) <= USER_PASSWORD_MAX_LENGTH


def name_validator(name: str):
    from ...config import USER_NAME_MIN_LENGTH, USER_NAME_MAX_LENGTH
    return USER_NAME_MIN_LENGTH <= len(name) <= USER_NAME_MAX_LENGTH


def phone_validator(phone_number: str):
    from phonenumbers import carrier, parse
    from phonenumbers.phonenumberutil import number_type
    return carrier._is_mobile(number_type(parse(phone_number)))


make_user = build_make_user(
    name_validtor=name_validator,
    email_validator=email_validator,
    password_validator=password_validator,
    phone_validator=phone_validator)

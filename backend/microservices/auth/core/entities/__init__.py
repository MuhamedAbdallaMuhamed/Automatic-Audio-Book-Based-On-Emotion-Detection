import sys
from os import path
sys.path.append(path.realpath(path.join(path.dirname(__file__), '../..')))


from .make_user import build_make_user
from .user import User
from .hash_password import hash_password
from .make_edit_user import build_edit_user
from .exception import *


def email_validator(email: str):
    # validate email
    from config import USER_EMAIL_MAX_LENGTH
    if len(email) > USER_EMAIL_MAX_LENGTH:
        raise EmailLengthLimitExceeded

    from ..usecases import get_user
    if get_user(email=email):
        raise EmailAlreadyExist

    if '.' not in email[-USER_NAME_MIN_LENGTH + 1:]:
        raise EmailNotValid

    from validate_email import validate_email
    is_valid = validate_email(email, check_mx=False)
    if not is_valid:
        raise EmailNotValid

    return True


def password_validator(password: str):
    # validate password
    from config import USER_PASSWORD_MAX_LENGTH, USER_PASSWORD_MIN_LENGTH
    if len(password) > USER_PASSWORD_MAX_LENGTH:
        raise PasswordLengthLimitExceeded

    if len(password) < USER_PASSWORD_MIN_LENGTH:
        raise PasswordMinLengthBeyondLimit

    return True


def name_validator(name: str):
    from config import USER_NAME_MIN_LENGTH, USER_NAME_MAX_LENGTH
    if len(name) > USER_NAME_MAX_LENGTH:
        raise NameLengthLimitExceeded

    if len(name) < USER_NAME_MIN_LENGTH:
        raise NameMinLengthBeyondLimit

    return True


def phone_validator(phone_number: str):
    from phonenumbers import carrier, parse
    from phonenumbers.phonenumberutil import number_type
    try:
        if not carrier._is_mobile(number_type(parse(phone_number))):
            raise PhoneNotValid

        return True
    except Exception:
        raise PhoneNotValid


def salt_generator():
    import uuid
    return uuid.uuid4().hex


def id_generator():
    import uuid
    return uuid.uuid4().hex


make_user = build_make_user(
    id_generator=id_generator,
    name_validator=name_validator,
    email_validator=email_validator,
    password_validator=password_validator,
    phone_validator=phone_validator,
    hash_password=hash_password,
    salt_generator=salt_generator)

edit_user = build_edit_user(
    name_validator=name_validator,
    email_validator=email_validator,
    password_validator=password_validator,
    phone_validator=phone_validator,
    hash_password=hash_password,
    salt_generator=salt_generator)

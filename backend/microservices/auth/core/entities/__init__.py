from .make_user import build_make_user
from .user import User


def email_validator(email):
    # vaidlate email
    pass


def password_validator(password):
    # vaidlate password
    pass


make_user = build_make_user(
    email_validator=email_validator,
    password_validator=password_validator)
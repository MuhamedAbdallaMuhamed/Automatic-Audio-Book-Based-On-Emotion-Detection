import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))

import secrets
from config import *


class Config(object):
    # FLASK SESSION AND COOKIES SECRET KEY
    SECRET_KEY = secrets.token_urlsafe(SECRET_KEY_LENGTH)

    # JWT CONFIG
    JWT_SECRET_KEY = secrets.token_urlsafe(SECRET_KEY_LENGTH)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ACCESS_TOKEN_EXPIRES = JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES
    JWT_REFRESH_TOKEN_EXPIRES = JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES

    # FLASK MAIL SERVER CONFIG
    MAIL_SERVER = SERVER_EMAIL
    MAIL_PORT = SERVER_EMAIL_PORT
    MAIL_USE_SSL = True
    MAIL_USERNAME = SERVER_EMAIL_USERNAME
    MAIL_PASSWORD = SERVER_EMAIL_PASSWORD

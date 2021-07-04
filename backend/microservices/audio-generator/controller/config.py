import sys
from os import path
import secrets
from config import *

sys.path.append(path.join(path.dirname(__file__), '..'))


class Config(object):
    # FLASK SESSION AND COOKIES SECRET KEY
    SECRET_KEY = secrets.token_urlsafe(SECRET_KEY_LENGTH)

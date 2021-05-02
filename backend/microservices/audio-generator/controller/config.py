import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))

import secrets
from config import *


class Config(object):
    # FLASK SESSION AND COOKIES SECRET KEY
    SECRET_KEY = secrets.token_urlsafe(SECRET_KEY_LENGTH)

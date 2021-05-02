import os

SECRET_KEY_LENGTH = 32
APP_PATH = os.environ.get('APP_DIRECTORY') or os.path.abspath('.')
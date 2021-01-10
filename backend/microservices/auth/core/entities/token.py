from datetime import datetime


class Token:
    def __init__(self, token: str):
        self.__token = token

    @property
    def token(self):
        return self.__token

from datetime import datetime


class Token:
    def __init__(self, token: str, expire_date: datetime):
        self.__token = token
        self.__expire_date = expire_date

    @property
    def token(self):
        return self.__token

    @property
    def expire_date(self):
        return self.__expire_date

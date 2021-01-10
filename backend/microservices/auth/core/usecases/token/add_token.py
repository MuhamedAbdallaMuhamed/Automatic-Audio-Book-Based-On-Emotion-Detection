from datetime import datetime
from core.entities import Token


def build_add_token(insert_token):
    def add_token(token: str, expire_date: datetime) -> bool:
        token = Token(token=token, expire_date=expire_date)
        return insert_token(token)
    return add_token

from datetime import datetime
from core.entities import Token


def build_add_token(insert_token):
    def add_token(token: str) -> bool:
        token = Token(token=token)
        return insert_token(token)
    return add_token

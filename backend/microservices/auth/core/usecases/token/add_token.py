from datetime import datetime


def build_add_token(insert_token):
    def add_token(token: str) -> bool:
        return insert_token(token)
    return add_token

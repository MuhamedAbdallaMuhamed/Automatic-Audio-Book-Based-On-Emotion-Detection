from datetime import datetime
from .admin import db
from ...config import *

class TokenDb:
    @staticmethod
    def insert_token(token: str, expire_date: datetime):
        db.collection(TOKEN_COLLECTION_NAME).add({
            TOKEN_TOKEN_ENTITY_NAME: token,
            TOKEN_EXPIRE_DATE_ENTITY_NAME: expire_date
        })
        return True

    @staticmethod
    def is_token_exist(token: str):
        docs = db.collection(TOKEN_COLLECTION_NAME).where(TOKEN_TOKEN_ENTITY_NAME, '==', token).stream()
        return len(docs) != 0

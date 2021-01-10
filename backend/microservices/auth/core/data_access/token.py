from datetime import datetime
from .admin import db
from ...config import *

class TokenDb:
    @staticmethod
    def insert_token(token: str):
        db.collection(TOKEN_COLLECTION_NAME).add({
            TOKEN_TOKEN_ENTITY_NAME: token,
        })
        return True

    @staticmethod
    def is_token_exist(token: str):
        docs = db.collection(TOKEN_COLLECTION_NAME).where(TOKEN_TOKEN_ENTITY_NAME, '==', token).stream()
        return len(docs) != 0

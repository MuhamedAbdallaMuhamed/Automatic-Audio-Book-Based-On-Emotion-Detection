from .admin import db
from ..entities import User
from ...config import *


class UserDb:
    @staticmethod
    def insert_user(user: User) -> bool:
        db.collection(USER_COLLECTION_NAME).document(user.id).set(user.to_dict())
        return True

    @staticmethod
    def get_user(id: str) -> User:
        u = db.collection(USER_COLLECTION_NAME).document(id).get().to_dict()
        user = User(
            id=u[USER_ID_ENTITY_NAME],
            first_name=u[USER_FIRST_NAME_ENTITY_NAME],
            last_name=u[USER_LAST_NAME_ENTITY_NAME],
            email=u[USER_EMAIL_ENTITY_NAME],
            password=u[USER_PASSWORD_ENTITY_NAME],
            phone=u[USER_PHONE_ENTITY_NAME],
            profile_picture_url=u[USER_PROFILE_PICTURE_URL_ENTITY_NAME],
        )
        return user

    @staticmethod
    def update_user(user: User) -> bool:
        db.collection(USER_COLLECTION_NAME).document(user.id).update(user.to_dict())
        return True

    @staticmethod
    def deleter_user(id: str) -> bool:
        db.collection(USER_COLLECTION_NAME).document(user.id).delete()
        return True

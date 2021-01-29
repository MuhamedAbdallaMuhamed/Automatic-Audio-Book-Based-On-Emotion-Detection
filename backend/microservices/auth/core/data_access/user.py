from .admin import db, image_ref, bucket
from ..entities import User
from config import *

import os

class UserDb:
    @staticmethod
    def add_image_to_storage(user_id, image_data):
        import base64
        #  removing meta data if it exists
        image_data = image_data.encode("ascii");
        if image_data.startswith(b'data:image'):
            idx = image_data.index(b',')
            image_data = image_data[idx + 1:]

        image_data = base64.b64decode(image_data)
        image_id = user_id
        filename = image_id + '.png'
        with open(filename, 'wb') as f:
            f.write(image_data)
        image_ref.child('images/' + user_id + '.png').put(filename, token=None)
        os.remove(filename)
        image_ref.child(filename).download(filename)
        return True

    @staticmethod
    def get_image_url(user_id):
        return image_ref.child('images/' + user_id + '.png').get_url(None)

    @staticmethod
    def insert_user(user: User) -> bool:
        db.collection(USER_COLLECTION_NAME).document(user.id).set(UserDb.user_to_dict(user))
        return True

    @staticmethod
    def get_user_by_id(id: str) -> User:
        u = db.collection(USER_COLLECTION_NAME).document(id).get().to_dict()
        if u:
            user = User(
                id=u[USER_ID_ENTITY_NAME],
                first_name=u[USER_FIRST_NAME_ENTITY_NAME],
                last_name=u[USER_LAST_NAME_ENTITY_NAME],
                email=u[USER_EMAIL_ENTITY_NAME],
                hashed_password=u[USER_HASHED_PASSWORD_ENTITY_NAME],
                salt=u[USER_SALT_ENTITY_NAME],
                phone=u[USER_PHONE_ENTITY_NAME],
                profile_picture_url=UserDb.get_image_url(u[USER_ID_ENTITY_NAME]),
                birthday=u[USER_BIRTHDAY_ENTITY_NAME],
                gender=u[USER_GENDER_ENTITY_NAME],
                password_reset_code=u[USER_PASSWORD_RESET_CODE_ENTITY_NAME]
            )
            return user
        return None

    @staticmethod
    def get_user_by_email(email: str) -> User:
        users = db.collection(USER_COLLECTION_NAME).where(USER_EMAIL_ENTITY_NAME, '==', email).stream()

        for u in users:
            u = u.to_dict()
            user = User(
                    id=u[USER_ID_ENTITY_NAME],
                    first_name=u[USER_FIRST_NAME_ENTITY_NAME],
                    last_name=u[USER_LAST_NAME_ENTITY_NAME],
                    email=u[USER_EMAIL_ENTITY_NAME],
                    hashed_password=u[USER_HASHED_PASSWORD_ENTITY_NAME],
                    salt=u[USER_SALT_ENTITY_NAME],
                    phone=u[USER_PHONE_ENTITY_NAME],
                    profile_picture_url=UserDb.get_image_url(u[USER_ID_ENTITY_NAME]),
                    birthday=u[USER_BIRTHDAY_ENTITY_NAME],
                    gender=u[USER_GENDER_ENTITY_NAME],
                    password_reset_code=u[USER_PASSWORD_RESET_CODE_ENTITY_NAME]
            )
            return user
        return None

    @staticmethod
    def update_user(user: User) -> bool:
        db.collection(USER_COLLECTION_NAME).document(user.id).update(UserDb.user_to_dict(user))
        return True

    @staticmethod
    def deleter_user(id: str) -> bool:
        db.collection(USER_COLLECTION_NAME).document(id).delete()
        return True

    @staticmethod
    def user_to_dict(user):
        return {
            USER_ID_ENTITY_NAME: user.id,
            USER_FIRST_NAME_ENTITY_NAME: user.first_name,
            USER_LAST_NAME_ENTITY_NAME: user.last_name,
            USER_EMAIL_ENTITY_NAME: user.email,
            USER_HASHED_PASSWORD_ENTITY_NAME: user.hashed_password,
            USER_SALT_ENTITY_NAME: user.salt,
            USER_PHONE_ENTITY_NAME: user.phone,
            USER_PROFILE_PICTURE_URL_ENTITY_NAME: user.profile_picture_url,
            USER_BIRTHDAY_ENTITY_NAME: user.birthday,
            USER_GENDER_ENTITY_NAME: user.gender,
            USER_PASSWORD_RESET_CODE_ENTITY_NAME: user.password_reset_code
        }

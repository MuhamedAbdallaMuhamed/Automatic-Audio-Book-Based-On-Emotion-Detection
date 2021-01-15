from .admin import db
from ..entities import UserBook
from ...config import *


class UserBookDb:
    @staticmethod
    def insert_user_book(user_book: UserBook) -> bool:
        db.collection(USER_BOOK_COLLECTION_NAME).document(user_book.id).set(UserBookDb.user_book_to_dict(user_book))
        return True

    @staticmethod
    def get_user_book_by_record_id(id: str) -> UserBook:
        ub = db.collection(USER_BOOK_COLLECTION_NAME).document(id).get().to_dict()
        user_book = UserBook(
            id=ub[USER_BOOK_ID_ENTITY_NAME],
            user_id=ub[USER_BOOK_USER_ID_ENTITY_NAME],
            book_id=ub[USER_BOOK_BOOK_ID_ENTITY_NAME],
            title=ub[USER_BOOK_TITLE_ENTITY_NAME]
        )
        return user_book

    @staticmethod
    def get_user_book_by_user_id(user_id: str):
        pass
        ub = db.collection(USER_BOOK_COLLECTION_NAME).where(USER_BOOK_USER_ID_ENTITY_NAME, '==', user_id).stream()
        if len(ub) == 0:
            return None
        ub = ub[0].to_dict()

    @staticmethod
    def update_user_book(user_book: UserBook) -> bool:
        db.collection(USER_BOOK_COLLECTION_NAME).document(user_book.id).update(UserBookDb.user_book_to_dict(user_book))
        return True

    @staticmethod
    def delete_user_book(id: str) -> bool:
        db.collection(USER_BOOK_COLLECTION_NAME).document(id).delete()
        return True

    @staticmethod
    def user_book_to_dict(user_book):
        return {
            USER_BOOK_ID_ENTITY_NAME: user_book.id,
            USER_BOOK_BOOK_ID_ENTITY_NAME: user_book.book_id,
            USER_BOOK_USER_ID_ENTITY_NAME: user_book.user_id,
            USER_BOOK_TITLE_ENTITY_NAME: user_book.title
        }
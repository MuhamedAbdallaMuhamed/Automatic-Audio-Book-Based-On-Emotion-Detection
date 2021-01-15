from .admin import db
from ..entities import Book
from ...config import *


class BookDb:
    @staticmethod
    def insert_book(book: Book) -> bool:
        db.collection(BOOK_COLLECTION_NAME).document(book.id).set(BookDb.book_to_dict(book))
        return True

    @staticmethod
    def get_book_by_id(id: str) -> Book:
        b = db.collection(BOOK_COLLECTION_NAME).document(id).get().to_dict()
        book = Book(
            id=b[BOOK_ID_ENTITY_NAME],
            book_hash=b[BOOK_HASH_ENTITY_NAME],
            book_path=b[BOOK_BOOK_PATH_ENTITY_NAME],
            sentence_features=b[BOOK_SENTENCE_FEATURES_ENTITY_NAME]
        )
        return book

    @staticmethod
    def get_book_by_book_hash(book_hash: str) -> Book:
        b = db.collection(BOOK_COLLECTION_NAME).where(BOOK_HASH_ENTITY_NAME, '==', book_hash).stream()

        if len(b) == 0:
            return None
        b = b[0].to_dict()

        book = Book(
            id=b[BOOK_ID_ENTITY_NAME],
            book_hash=b[BOOK_HASH_ENTITY_NAME],
            book_path=b[BOOK_BOOK_PATH_ENTITY_NAME],
            sentence_features=b[BOOK_SENTENCE_FEATURES_ENTITY_NAME]
        )
        return book

    @staticmethod
    def update_book(book: Book) -> bool:
        db.collection(BOOK_COLLECTION_NAME).document(book.id).update(BookDb.book_to_dict(book))
        return True

    @staticmethod
    def delete_book(id: str) -> bool:
        db.collection(BOOK_COLLECTION_NAME).document(id).delete()
        return True

    @staticmethod
    def book_to_dict(book):
        return {
            BOOK_ID_ENTITY_NAME: book.id,
            BOOK_HASH_ENTITY_NAME: book.book_hash,
            BOOK_BOOK_PATH_ENTITY_NAME: book.book_path,
            BOOK_SENTENCE_FEATURES_ENTITY_NAME: book.sentence_features
        }

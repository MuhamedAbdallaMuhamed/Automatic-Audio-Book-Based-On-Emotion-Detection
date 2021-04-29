from typing import Optional

from flask import jsonify

from core.data_access.admin import db
from ..entities import Book
from config import *


class BookDb:
    @staticmethod
    def insert_book(book: Book) -> bool:
        db.collection(BOOK_COLLECTION_NAME).document(book.id).set(BookDb.book_to_dict(book))
        return True

    @staticmethod
    def get_book_by_id(id: str) -> Optional[Book]:
        try:
            b = db.collection(BOOK_COLLECTION_NAME).document(id).get().to_dict()
            if b:
                book = Book(
                    id=b[BOOK_ID_ENTITY_NAME],
                    book_hash=b[BOOK_HASH_ENTITY_NAME],
                    book_path=b[BOOK_BOOK_PATH_ENTITY_NAME],
                    sentence_features=b[BOOK_SENTENCE_FEATURES_ENTITY_NAME],
                    name=b[BOOK_NAME_ENTITY_NAME]
                )
                return book
            return None
        except Exception as e:
            print(e)

    @staticmethod
    def get_book_by_book_hash(book_hash: str) -> Book:
        books = db.collection(BOOK_COLLECTION_NAME).where(BOOK_HASH_ENTITY_NAME, '==', book_hash).stream()

        for b in books:
            bb = b.to_dict()
            book = Book(
                id=bb[BOOK_ID_ENTITY_NAME],
                book_hash=bb[BOOK_HASH_ENTITY_NAME],
                book_path=bb[BOOK_BOOK_PATH_ENTITY_NAME],
                sentence_features=bb[BOOK_SENTENCE_FEATURES_ENTITY_NAME],
                name=bb[BOOK_NAME_ENTITY_NAME]
            )
            return book
        return None

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
            BOOK_SENTENCE_FEATURES_ENTITY_NAME: book.sentence_features,
            BOOK_NAME_ENTITY_NAME: book.name
        }

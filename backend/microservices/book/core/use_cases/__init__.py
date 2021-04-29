from datetime import datetime
from core.entities import Book
from core.entities import UserBook
from core.data_access.book import *
from core.data_access.user_book import *
from core.data_access import *
from core.use_cases.book import *
from core.use_cases.user_book import *


def insert_book(book) -> bool:
    return BookDb.insert_book(book)


def get_book_by_id(id) -> Book:
    return BookDb.get_book_by_id(id)


def get_book_by_book_hash(book_hash) -> Book:
    return BookDb.get_book_by_book_hash(book_hash)


def update_book(book) -> bool:
    return BookDb.update_book(book)


def delete_book(id) -> bool:
    return BookDb.delete_book(id)


def book_to_dict(book: Book):
    return BookDb.book_to_dict(book)


def insert_user_book(user_book) -> bool:
    return UserBookDb.insert_user_book(user_book)


def delete_user_book(id) -> bool:
    return UserBookDb.delete_user_book(id)


def get_user_book_by_id(id) -> UserBook:
    return UserBookDb.get_user_book_by_record_id(id)


add_book = build_add_book(insert_book=insert_book)
get_book = build_get_book(get_book_by_id=get_book_by_id, get_book_by_hash=get_book_by_book_hash)
update_book = build_update_book(update_book=update_book)
delete_book = build_delete_book(delete_book=delete_book)

add_user_book = build_add_user_book(insert_user_book=insert_user_book)
get_user_book = build_get_user_book(get_user_book_by_id=get_user_book_by_id)
delete_user_book = build_delete_user_book(delete_user_book=delete_user_book)



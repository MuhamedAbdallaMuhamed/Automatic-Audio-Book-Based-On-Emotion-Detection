from datetime import datetime
from ..entities import Book
from ..entities import UserBook
from .book import *
from .user_book import *
from ..data_access import *


def insert_book(book) -> bool:
    return BookDb.insert_book(book)


def get_book_by_id(id) -> Book:
    return BookDb.get_book_by_id(id)


def get_book_by_book_hash(book_hash) -> Book:
    return BookDb.get_book_by_book_hash(book_hash)


def update_book(book) -> bool:
    return BookDb.update_book(book)


def delete_book(id) -> bool:
    return BookDb.deleter_book(id)


def insert_user_book(user_book) -> bool:
    return UserBookDb.insert_user_book(user_book)


def delete_book(id) -> bool:
    return UserBookDb.deleter_user_book(id)


def get_user_book_by_record_id(id)->UserBook:
    return UserBookDb.get_user_book_by_record_id(id)


add_book = build_add_book(insert_book=insert_book)
get_book = build_get_book(get_book_by_id=get_book_by_id, get_book_by_hash=get_book_by_book_hash)
update_book = build_update_book(update_book=update_book)
delete_book = build_delete_book(delete_book=delete_book)

add_user_book = build_add_user_book(insert_user_book=insert_user_book)
get_user_book = build_get_user_book(get_user_book_by_id=get_user_book_by_record_id)
delete_user_book = build_delete_user_book(delete_user_book=delete_user_book)



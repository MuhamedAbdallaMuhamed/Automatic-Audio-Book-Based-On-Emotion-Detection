from .make_book import build_make_book
from .make_edit_book import build_make_edit_book
from .Book import Book
from .UserBook import UserBook
from .make_user_book import build_make_user_book
from .exception import *


def name_validator(name: str):
    if len(name) > 50:
        raise NameLengthLimitExceededException
    return True


def book_hash_validator(book_hash: str):
    return True


def book_path_validator(book_path: str):
    return True


def sentence_features_validator(sentence_features: str):
    return True


def book_validator(book_id: str):
    from ..use_cases import get_book_by_id
    if get_book_by_id(book_id):
        return True
    return False


def user_validator(user_id: str):
    #TODO: get_user_by_id
    return True


def title_validator(title: str):
    if len(title) > 50:
        raise NameLengthLimitExceededException
    return True


def id_generator():
    import uuid
    return uuid.uuid4()


make_book = build_make_book(
    id_generator=id_generator,
    name_validator=name_validator,
    book_hash_validator=book_hash_validator,
    book_path_validator=book_path_validator,
    sentence_features_validator=sentence_features_validator,
)

edit_book = build_make_edit_book(
    name_validator=name_validator,
    book_hash_validator=book_hash_validator,
    book_path_validator=book_path_validator,
    sentence_features_validator=sentence_features_validator,
)

make_user_book = build_make_user_book(
    id_generator=id_generator,
    book_validator=book_validator,
    user_validator=user_validator,
    title_validator=title_validator
)

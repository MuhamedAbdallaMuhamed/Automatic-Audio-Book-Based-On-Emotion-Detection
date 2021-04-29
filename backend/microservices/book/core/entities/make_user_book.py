from .UserBook import UserBook
from .exception import *


def build_make_user_book(id_generator, book_validator, user_validator, title_validator):
    def make_user_book(book_id, user_id, title):
        # validate book
        if not book_validator(book_id):
            raise BookNotFoundException

        # validate user
        if not user_validator(user_id):
            raise UserNotFoundException

        # validate title
        if not title_validator(title):
            raise NameLengthLimitExceededException

        user_book = UserBook(
            id=id_generator(),
            title=title,
            book_id=book_id,
            user_id=user_id
        )
        return user_book

    return make_user_book

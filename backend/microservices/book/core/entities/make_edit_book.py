from .Book import Book
from .exception import *


def build_make_edit_book(name_validator, book_hash_validator, book_path_validator, sentence_features_validator):
    def make_edit_book(id, name, book_hash, book_path, sentence_features):
        # validate name
        if not name_validator(name):
            raise NameLengthLimitExceededException

        # validate book_hash
        if not book_hash_validator(book_hash):
            raise BookHashNotValidException

        # validate book_path
        if not book_path_validator(book_path):
            raise BookPathNotValidException

        # validate sentence_features
        if not sentence_features_validator(sentence_features):
            raise SentenceFeaturesValidException

        book = Book(
            id=id,
            name=name,
            book_hash=book_hash,
            book_path=book_path,
            sentence_features=sentence_features,
        )
        return book

    return make_edit_book

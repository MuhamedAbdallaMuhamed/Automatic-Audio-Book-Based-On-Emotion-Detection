from ...entities import edit_book
from .. import get_book


def build_update_book(update_book):
    def update_book(id=None, name=None, book_hash=None, book_path=None, sentence_features=None) -> bool:
        if not id:
            # TODO: throw error
            pass

        old_book = get_book(id=id)
        if not old_book:
            # TODO: throw error
            pass

        edited_book = edit_book(
            id=old_book.id,
            name=name if name else old_book.name,
            book_hash=book_hash if book_hash else old_book.book_hash,
            book_path=book_path if book_path else old_book.book_path,
            sentence_features=sentence_features if sentence_features else old_book.sentence_features,

            new_name=name is not None,
            new_book_hash=book_hash is not None,
            new_book_path=book_path is not None,
            new_sentence_features=sentence_features is not None,
        )

        return update_book(edited_book)

    return update_book

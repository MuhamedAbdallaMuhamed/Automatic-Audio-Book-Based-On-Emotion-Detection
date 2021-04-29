from ...entities import edit_book


def build_update_book(update_book):
    def update_book_(id=None, name=None, book_hash=None, book_path=None, sentence_features=None) -> bool:
        if not id:
            # TODO: throw error
            pass
        from .. import get_book
        old_book = get_book(id=id, book_hash=None)
        if old_book is None:
            # TODO: throw error
            print("None")
            return None

        edited_book = edit_book(
            id=old_book.id,
            name=name if name else old_book.name,
            book_hash=book_hash if book_hash else old_book.hash,
            book_path=book_path if book_path else old_book.book_path,
            sentence_features=sentence_features if sentence_features else old_book.sentence_features,
        )

        return update_book(edited_book)

    return update_book_

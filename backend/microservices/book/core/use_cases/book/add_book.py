from ...entities import make_book


def build_add_book(insert_book):
    def add_book(id, name, book_hash, book_path, sentance_features) -> bool:
        book = make_book(id, name, book_hash, book_path, sentance_features)
        return insert_book(book)

    return add_book

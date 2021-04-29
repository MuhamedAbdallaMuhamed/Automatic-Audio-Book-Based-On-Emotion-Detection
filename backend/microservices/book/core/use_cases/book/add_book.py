from ...entities import make_book


def build_add_book(insert_book):
    def add_book(name, book_hash, book_path, sentence_features) -> bool:
        book = make_book(name, book_hash, book_path, sentence_features)
        return insert_book(book)

    return add_book

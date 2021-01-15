from ...entities import Book


def build_get_book(get_book_by_id, get_book_by_hash):
    def get_book(id: str = None, book_hash: str = None) -> Book:
        return get_book_by_id(id) if id else get_book_by_hash(book_hash)
    return get_book
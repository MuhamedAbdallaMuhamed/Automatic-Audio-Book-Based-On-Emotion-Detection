from ...entities import make_user_book


def build_add_user_book(insert_user_book):
    def add_user_book(id, book_id, user_id, title) -> bool:
        book = make_user_book(id, book_id, user_id, title)
        return insert_user_book(book)

    return add_user_book

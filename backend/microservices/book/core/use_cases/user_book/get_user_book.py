from ...entities import UserBook


def build_get_user_book(get_user_book_by_id):
    def get_user_book(id: str = None) -> UserBook:
        return get_user_book_by_id(id)

    return get_user_book

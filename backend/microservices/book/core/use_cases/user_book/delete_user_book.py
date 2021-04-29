def build_delete_user_book(delete_user_book):
    def delete_user_book_(id) -> bool:
        return delete_user_book(id)

    return delete_user_book_

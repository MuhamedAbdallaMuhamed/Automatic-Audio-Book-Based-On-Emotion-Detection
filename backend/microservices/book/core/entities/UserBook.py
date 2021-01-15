class UserBook:
    def __init__(self, id, book_id, user_id, title):
        self.__id = id
        self.__book_id = book_id
        self.__user_id = user_id
        self.__title = title

    @property
    def id(self):
        return self.__id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def title(self):
        return self.__title

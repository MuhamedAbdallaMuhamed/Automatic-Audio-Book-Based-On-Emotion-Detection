from config import BOOK_TITLE_MAX_LENGTH, BOOK_TITLE_MIN_LENGTH


class BookTItleException(Exception):
    """Exception raised when title's length exceeds the allowed length"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'there is something wrong with the title.'


class BookTitleLengthLimitExceeded(BookTItleException):
    """Exception raised when titles's length exceeds the allowed length"""

    def __init__(self, name=None):
        self.name = name
        super().__init__(self.__str__())

    def __str__(self):
        if self.name:
            return f'"{self.name}" exceeded the allowed length ({BOOK_TITLE_MAX_LENGTH}).'
        return 'The name Length exceeded the allowed length.'


class BookTitleMinLengthBeyondLimit(BookTItleException):
    """Exception raised when name's length < name min length"""

    def __init__(self, name=None):
        self.name = name
        super().__init__(self.__str__())

    def __str__(self):
        if self.name:
            return f'"{self.name}" beyond the allowed length ({BOOK_TITLE_MIN_LENGTH}).'
        return 'The name Length beyond the allowed length.'


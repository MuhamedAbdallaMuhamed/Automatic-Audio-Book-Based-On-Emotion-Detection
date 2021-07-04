class PageNumberException(Exception):
    """Exception raised when page number is invalid"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'there is something wrong with the starting or ending page number.'


class PageNumberBeyondLimit(PageNumberException):
    """Exception raised when page number < 1"""

    def __init__(self, page_number=None):
        self.page_number = page_number
        super().__init__(self.__str__())

    def __str__(self):
        if self.page_number:
            return f'the page number "{self.page_number}" beyond the limits "-1").'
        return 'The page number beyond the limits "-1".'


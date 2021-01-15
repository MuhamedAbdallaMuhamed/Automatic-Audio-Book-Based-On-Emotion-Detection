class BookPathNotValidException(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, book_path=None):
        self.book_path = book_path
        super().__init__(self.__str__())

    def __str__(self):
        if self.book_path:
            return f'"{self.book_path}" is not a valid path.'
        return 'The book path is not a valid path.'

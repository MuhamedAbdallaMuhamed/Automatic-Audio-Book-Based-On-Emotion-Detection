class BookHashNotValidException(Exception):
    """Exception raised for not valid string"""

    def __init__(self, book_hash=None):
        self.book_hash = book_hash
        super().__init__(self.__str__())

    def __str__(self):
        return 'The book hash is not a valid hash.'

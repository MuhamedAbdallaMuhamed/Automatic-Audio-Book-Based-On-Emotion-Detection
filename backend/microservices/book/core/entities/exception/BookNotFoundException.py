class BookNotFoundException(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, book_id=None):
        self.book_id = book_id
        super().__init__(self.__str__())

    def __str__(self):
        return 'The book is not found.'

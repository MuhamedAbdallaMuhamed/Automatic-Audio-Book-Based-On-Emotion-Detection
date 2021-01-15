class UserNotFoundException(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, user_id=None):
        self.user_id = user_id
        super().__init__(self.__str__())

    def __str__(self):
        return 'The User is not found.'

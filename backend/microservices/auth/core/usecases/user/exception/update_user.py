class UserException(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'there is something wrong with the user.'


class UserDoesNotExist(UserException):
    """Exception raised for non phones string's"""

    def __init__(self, identity=None):
        self.identity = identity
        super().__init__(self.__str__())

    def __str__(self):
        if self.identity:
            return f'"{self.identity}" not an actual user.'
        return 'User does not exist.'

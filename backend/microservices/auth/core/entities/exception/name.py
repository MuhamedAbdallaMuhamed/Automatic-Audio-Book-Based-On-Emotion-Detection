from config import USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH


class NameException(Exception):
    """Exception raised when name's length exceeds the allowed length"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'there is something wrong with the name.'


class NameLengthLimitExceeded(NameException):
    """Exception raised when name's length exceeds the allowed length"""

    def __init__(self, name=None):
        self.name = name
        super().__init__(self.__str__())

    def __str__(self):
        if self.name:
            return f'"{self.name}" exceeded the allowed length ({USER_NAME_MAX_LENGTH}).'
        return 'The name Length exceeded the allowed length.'


class NameMinLengthBeyondLimit(NameException):
    """Exception raised when name's length < email min length"""

    def __init__(self, name=None):
        self.name = name
        super().__init__(self.__str__())

    def __str__(self):
        if self.name:
            return f'"{self.name}" exceeded the allowed length ({USER_NAME_MIN_LENGTH}).'
        return 'The name Length exceeded the allowed length.'


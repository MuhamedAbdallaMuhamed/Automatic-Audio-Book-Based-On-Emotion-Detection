from config import USER_EMAIL_MAX_LENGTH


class EmailException(Exception):
    """Email Exception base class"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'There is something wrong with the email'


class EmailNotValid(EmailException):
    """Exception raised for non emails string's"""

    def __init__(self, email=None):
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        if self.email:
            return f'"{self.email}" is not a valid email.'
        return 'The email is not a valid email.'


class EmailLengthLimitExceeded(EmailException):
    """Exception raised when email's length exceeds the allowed length"""

    def __init__(self, email=None):
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        if self.email:
            return f'"{self.email}" exceeded the allowed length ({USER_EMAIL_MAX_LENGTH}).'
        return 'The email is not a valid email.'


class EmailAlreadyExist(EmailException):
    """Exception raised if the email already exist"""

    def __init__(self, email=None):
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        if self.email:
            return f'"{self.email}" is already exist.'
        return 'The email is exist email.'

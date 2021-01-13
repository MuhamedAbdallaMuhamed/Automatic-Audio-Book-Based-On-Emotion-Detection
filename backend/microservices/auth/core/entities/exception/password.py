from config import USER_PASSWORD_MAX_LENGTH


class PasswordLengthLimitExceeded(Exception):
    """Exception raised when password's length exceeds the allowed length"""

    def __init__(self, password=None):
        self.password = password
        super().__init__(self.__str__())

    def __str__(self):
        if self.password:
            return f'"{self.password}" exceeded the allowed length ({USER_PASSWORD_MAX_LENGTH}).'
        return 'The password Length exceeded the allowed length.'

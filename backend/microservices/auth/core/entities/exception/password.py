class PasswordLengthLimitExceeded(Exception):
    """Exception raised when password's length exceeds the allowed length"""

    def __init__(self, password=None):
        self.password = password
        super().__init__(self.__str__())

    def __str__(self):
        if self.password:
            return f'"{self.password}" exceeded the allowed length.'
        return 'The password Length exceeded the allowed length.'

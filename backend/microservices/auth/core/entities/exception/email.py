class EmailNotValid(Exception):
    """Exception raised for non emails string's"""

    def __init__(self, email=None):
        self.email = email
        super().__init__(self.__str__())

    def __str__(self):
        if self.email:
            return f'"{self.email}" is not a valid email.'
        return 'The email is not a valid email.'

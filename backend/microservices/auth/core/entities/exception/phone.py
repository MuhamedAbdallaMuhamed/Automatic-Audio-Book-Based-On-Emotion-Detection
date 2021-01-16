class PhoneException(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return 'there is something wrong with the phone.'


class PhoneNotValid(PhoneException):
    """Exception raised for non phones string's"""

    def __init__(self, phone=None):
        self.phone = phone
        super().__init__(self.__str__())

    def __str__(self):
        if self.phone:
            return f'"{self.phone}" is not a valid phone.'
        return 'The phone is not a valid phone.'

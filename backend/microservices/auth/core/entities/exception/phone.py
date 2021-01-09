class PhoneNotValid(Exception):
    """Exception raised for non phones string's"""

    def __init__(self, phone=None):
        self.phone = phone
        super().__init__(self.__str__())

    def __str__(self):
        if self.phone:
            return f'"{self.phone}" is not a valid phone.'
        return 'The phone is not a valid phone.'

class NameLengthLimitExceededException(Exception):
    """Exception raised when name's length exceeds the allowed length"""

    def __init__(self, name=None):
        self.name = name
        super().__init__(self.__str__())

    def __str__(self):
        if self.name:
            return f'"{self.name}" exceeded the allowed length.'
        return 'The name Length exceeded the allowed length.'

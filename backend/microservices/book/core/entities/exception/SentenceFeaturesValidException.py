class SentenceFeaturesValidException(Exception):
    """Exception raised for non sentence string"""

    def __init__(self, sentence_features=None):
        self.sentence_features = sentence_features
        super().__init__(self.__str__())

    def __str__(self):
        return 'The sentence is not a valid string.'

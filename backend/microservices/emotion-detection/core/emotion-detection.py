class EmotionDetection:
    def __init__(self, sentence_array):
        self.__sentence_array = sentence_array
        self.__emotion_array = None

    @property
    def getEmotions(self):
        return self.__emotion_array

    @property
    def performEmotionDetection(self):
        pass

    def _extractFeatures(self):
        pass

    def _performClassification(self):
        pass

    def _testAccuracy(self):
        pass

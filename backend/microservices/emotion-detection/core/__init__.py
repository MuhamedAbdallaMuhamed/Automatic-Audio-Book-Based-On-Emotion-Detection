from .emotion_detection_factory import makeEmotionDetection


def cleanSentences():
    pass


emotions = makeEmotionDetection(
    cleanSentences=cleanSentences()
)

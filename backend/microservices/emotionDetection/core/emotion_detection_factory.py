from .emotion_detection import EmotionDetection


def makeEmotionDetection(cleanSentences):
    def emotionDetection(sentences):
        sentences = cleanSentences(sentences)
        emotions = EmotionDetection(sentences)

        # perform emotion detection
        emotions.performEmotionDetection()

        return emotions.getEmotions

    return emotionDetection

import text2emotion


def get_highest_emotion(emotions):
    highest_emotion = ""
    max_val = 0
    for e in emotions:
        if emotions[e] >= max_val:
            max_val = emotions[e]
            highest_emotion = e
    return highest_emotion


def getEmotion(sentence):
    emotions = text2emotion.get_emotion(sentence)
    return get_highest_emotion(emotions)

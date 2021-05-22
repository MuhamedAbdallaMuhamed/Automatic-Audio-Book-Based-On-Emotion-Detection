from flask import Flask, jsonify, request, Blueprint, Response
import text2emotion

# initializing FLASK
app = Flask(__name__)

# initializing api
api_bp = Blueprint('api', __name__)

app.register_blueprint(api_bp)


def get_highest_emotion(emotion):
    highest_emotion = ""
    max_val = 0
    for e in emotion:
        if emotion[e] > max_val:
            max_val = emotion[e]
            highest_emotion = e
    return highest_emotion


@app.route('/emotion-detection/get-text-emotion', methods=['POST'])
def GetEmotions():
    request_body = request.get_json()
    sentences = request_body["Sentences"]
    emotions = []
    for sentence in sentences:
        emotion = text2emotion.get_emotion(sentence)

        emotions.append(get_highest_emotion(emotion))
    # text = "I was asked to sign a third party contract a week out from stay. If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury."
    # emotions = text2emotion.get_emotion(text)
    return jsonify(emotions)

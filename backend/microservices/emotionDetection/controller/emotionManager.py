from flask_restful import Resource, fields, reqparse, marshal_with
from ..core import emotions
from .. import api
from ..config import *

detection_fields = {
    TOKENS_KEY: fields.String(attribute=lambda x: x.token),
    SENTENCES_KEY: fields.List(attribute=lambda x: x.data)
}

detection_filter_parser = reqparse.RequestParser()
detection_filter_parser.add_argument(TOKENS_KEY, type=str, required=False)
detection_filter_parser.add_argument(SENTENCES_KEY, type=list, required=False)


class EmotionDetectionController(Resource):
    @marshal_with(detection_fields)
    def get(self):
        detection = detection_filter_parser.parse_args()
        '''
        Check token of user here
        TODO: After getting api
        '''
        emotion_array = emotions(detection[SENTENCES_KEY])
        return {EMOTION_KEY: emotion_array}


api.add_resource(EmotionDetectionController, EMOTION_DETECTION_SERVER)

from flask_restful import Resource, fields, reqparse, marshal_with
from ..core import emotions
from .. import api

detection_fields = {
    'token': fields.String(attribute=lambda x: x.token),
    'data': fields.List(attribute=lambda x: x.data)
}

detection_filter_parser = reqparse.RequestParser()
detection_filter_parser.add_argument('token', type=str, required=False)
detection_filter_parser.add_argument('data', type=list, required=False)


class EmotionDetectionController(Resource):
    @marshal_with(detection_fields)
    def get(self):
        detection = detection_filter_parser.parse_args()
        '''
        Check token of user here
        TODO: After getting api
        '''
        emotion_array = emotions(detection['data'])
        return {'emotions': emotion_array}


api.add_resource(EmotionDetectionController, '/emotion-detection')

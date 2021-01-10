from flask_restful import Resource
from flask_jwt_extended import jwt_required , get_raw_jwt

from . import api
from config import *

class LogoutResource(Resource):

    @jwt_required
    def post(self):
        # parsing the coming request
        jti = get_raw_jwt()['jti']

        # TODO: add the token to blocked JWT

        return {
            MESSAGE_HEADER_NAME: 'Logged out successfully'
        }


api.add_resource(LogoutResource, LOGOUT_ABS_ENDPOINT_NAME)

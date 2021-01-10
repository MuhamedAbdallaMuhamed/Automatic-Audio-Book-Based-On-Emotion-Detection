from flask_restful import Resource
from flask_jwt_extended import jwt_required , get_raw_jwt

from . import api, jwt
from config import *
from core.usecases import *


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return is_token_exist(jti)


class LogoutResource(Resource):
    @jwt_required
    def post(self):
        # parsing the coming request
        jti = get_raw_jwt()['jti']
        insert_token(token=jti)
        return {
            MESSAGE_HEADER_NAME: 'Logged out successfully'
        }


api.add_resource(LogoutResource, LOGOUT_ABS_ENDPOINT_NAME)

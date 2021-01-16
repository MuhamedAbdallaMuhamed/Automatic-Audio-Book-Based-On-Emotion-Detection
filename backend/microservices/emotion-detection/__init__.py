from flask import Flask, Blueprint
from flask_restful import Api
from .config import *

app = Flask(__name__)
app.config[SECRET_KEY] = SECRET_VALUE

api_protocol = Blueprint(API_KEY, __name__, url_prefix=API_SERVER)
api = Api(api_protocol)
app.register_blueprint(api_protocol)

from .controller import *

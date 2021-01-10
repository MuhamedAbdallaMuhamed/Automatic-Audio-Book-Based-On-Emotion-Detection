from flask import Flask, Blueprint
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASCX1234asdas6SAD'

api_protocol = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_protocol)
app.register_blueprint(api_protocol)

from .controller import *

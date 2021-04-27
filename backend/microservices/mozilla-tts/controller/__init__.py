from flask import Flask, Blueprint
from flask_restful import Api

from .config import Config

# initializing FLASK
app = Flask(__name__)
app.config.from_object(Config)

# # initializing api
api_bp = Blueprint('api', __name__);
api = Api(api_bp)


from .routes import *
app.register_blueprint(api_bp)

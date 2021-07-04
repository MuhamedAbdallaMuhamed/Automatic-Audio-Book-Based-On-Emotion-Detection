from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from .config import Config

# initializing FLASK
app = Flask(__name__)
app.config.from_object(Config)

# initializing JSON web token
jwt = JWTManager(app)

# initializing mail service
mail = Mail(app)

# initializing api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


from .routes import *
app.register_blueprint(api_bp)

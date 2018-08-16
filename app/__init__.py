from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
from flask_cors import CORS


app = Flask(__name__)
""" Initialize the flask application """
CORS(app)
""" Enable CORS on the app """


app.config.from_object(config['development'])
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'alibaba'

from .api import apiv1
app.register_blueprint(apiv1, url_prefix='/api/v1')

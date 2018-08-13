from flask import Flask
from flask_jwt_extended import JWTManager
from config import config


app = Flask(__name__)
""" Initialize the flask application """
from app.api.database import DatabaseConnection
db = DatabaseConnection()
db.create_table_users()
db.create_table_entries()
""" Create the tables for users and entries """

app.config.from_object(config['development'])
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'alibaba'

from .api import apiv1
app.register_blueprint(apiv1, url_prefix='/api/v1')

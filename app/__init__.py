from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
from app.api.database import DatabaseConnection

db = DatabaseConnection()
db.create_table_entries()
db.create_table_users()
app = Flask(__name__)

app.config.from_object(config['development'])
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'alibaba'

from .api import apiv1
app.register_blueprint(apiv1, url_prefix='/api/v1')



from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])


from .api import apiv1
app.register_blueprint(apiv1, url_prefix='/api/v1')



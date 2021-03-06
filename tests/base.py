import unittest
import json
from datetime import timedelta
from flask_jwt_extended import create_access_token
from config import config
from app import app
from app.api.models.users import User
from app.api.database import DatabaseConnection


class BaseTestCase(unittest.TestCase):
    
    def setUp(self):   
        """ Set up the test environment """
        app.config['TESTING'] = True   
        DatabaseConnection.__init__(self)            
        self.app = app.test_client()
        with app.test_request_context():
            database_connection = DatabaseConnection()
            database_connection.drop_table_users()
            database_connection.drop_table_entries()            
            database_connection.create_table_users()
            database_connection.create_table_entries()
            self.token = create_access_token(identity=1)
            self.header = {"Authorization" : "Bearer {}". format(self.token)}  



    def tearDown(self):
        """ Tear down the test environment after the test """
        with app.test_request_context():
            database_connection = DatabaseConnection()
            database_connection.drop_table_users()
            database_connection.drop_table_entries()
            database_connection.stop_connection()

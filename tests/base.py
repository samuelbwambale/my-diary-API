import unittest
import json
from datetime import timedelta
from flask_jwt_extended import create_access_token
from app import app
from app.api.models.users import User
from app.api.database import DatabaseConnection


class BaseTestCase(unittest.TestCase):
    
    def setUp(self):         
        DatabaseConnection.__init__(self)       
        self.app = app.test_client()
        with app.test_request_context():
            database_connection = DatabaseConnection()
            database_connection.create_table_users()
            database_connection.create_table_entries()


            self.token = create_access_token(identity=1)
            self.header = {"Authorization" : "Bearer {}". format(self.token)}  


    def tearDown(self):
        database_connection = DatabaseConnection()
        database_connection.cursor.execute("DELETE FROM users")
        database_connection.cursor.execute("DELETE FROM users")

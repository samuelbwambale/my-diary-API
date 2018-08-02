import unittest
import json
from datetime import timedelta
from flask_jwt_extended import create_access_token
from app import app
from app.api.models.users import User
from app.api.database import DatabaseConnection


class BaseTestCase(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        with app.app_context():
            database_connection = DatabaseConnection()
            database_connection.create_table_users()
            database_connection.create_table_entries()

            user = {
            "first_name": "Alex",
            "last_name": "Fergurson",
            "email": "alexf@gmail.com", 
            "password": "password",
            }
            self.app.post("/api/v1/auth/signup",\
            data=json.dumps(user), content_type='application/json')

            logins = {
            "email": "newsboy@gmail.com", 
            "password": "password",
            }
            response = self.app.post("/api/v1/auth/login",\
            data=json.dumps(logins), content_type='application/json')
            #self.token = json.loads(response.get_data(as_text=True))["Token"]
            #self.headers = {"Authorization}" : "Bearer {}". format(self.token)}        


    def tearDown(self):
        database_connection = DatabaseConnection()
        database_connection.cursor.execute("DELETE FROM users")
        database_connection.cursor.execute("DELETE FROM users")

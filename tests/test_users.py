import unittest
import json
from tests.base import BaseTestCase
from app.api.models.users import User


user = {
            "first_name": "Isaac",
            "last_name": "Newton",
            "email": "newsboy@gmail.com", 
            "password": "password",
        }

user2 = {
            "first_name": "Isaac",
            "last_name": "Newton",
            "email": "newsboy@gmail.com", 
            "password": "password",
        }

logins = {
            "email": "newsboy@gmail.com", 
            "password": "password",
        }

class UsersApiTestCase(BaseTestCase):

    def test_register_user(self):
        response = self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')        
        self.assertEqual(response.status_code, 201)


    def test_register_with_duplicated_email(self):
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')
        response = self.app.post("/api/v1/auth/signup",
        data=json.dumps(user2), content_type='application/json')        
        self.assertEqual(response.status_code, 400)

    def test_register_with_with_invalid_email(self):
        user = {
            "first_name": "Isaac",
            "last_name": "Newton",
            "email": "newsboygmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')        
        self.assertEqual(response.status_code, 400)

    
    def test_register_user_with_missing_fields(self):
        usr = {
            "first_name": "Isaac",
            "email": "isaac@gmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",
            data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_register_user_with_empty_fields(self):
        usr = {
            "first_name": "Allan",
            "last_name": "Obore",
            "email": "obore@gmail.com", 
            "password": "",
        }
        response = self.app.post("/api/v1/auth/signup",
        data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')
        response = self.app.post("/api/v1/auth/login",
        data=json.dumps(logins), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

    def test_login_with_wrong_email(self):
        logins = {
            "email": "news@gmail.com", 
            "password": "password",
        }
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')
        response = self.app.post("/api/v1/auth/login",
        data=json.dumps(logins), content_type='application/json')
        self.assertEqual(response.status_code, 401)


    def test_login_with_wrong_password(self):
        logins = {
            "email": "newsboy@gmail.com", 
            "password": "password22",
        }
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')
        response = self.app.post("/api/v1/auth/login",
        data=json.dumps(logins), content_type='application/json')
        self.assertEqual(response.status_code, 401)


    def test_get_all_users(self):
        response = self.app.get('/api/v1/users', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_by_email(self):
        user = {
            "first_name": "Isaac",
            "last_name": "Newton",
            "email": "newsboy@gmail.com", 
            "password": "password",
        }
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')
        user = User(None,None,None,None)
        Found = False
        usr = user.get_user_by_email("newsboy@gmail.com")
        if usr:
            Found = True       
        self.assertEqual(Found, True)
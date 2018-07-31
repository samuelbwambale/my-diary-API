import unittest
import json
from tests.base import BaseTestCase
from app.api.resources.users_resource import USERS

class UsersApiTestCase(BaseTestCase):

    def test_register_user(self):
        user = {
            "first_name": "Isaac",
            "last_name": "Newton",
            "email": "example@gmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(user), content_type='application/json')        
        self.assertEqual(response.status_code, 201)
    
    def test_register_with_duplicated_email(self):
        usr = {
            "first_name": "Alice",
            "last_name": "Ayu",
            "email": "example@gmail.com", 
            "password": "password",
        }
        self.app.post("/api/v1/auth/signup",\
        data=json.dumps(usr), content_type='application/json')
        usr2 = {
            "first_name": "Ale",
            "last_name": "Ayu",
            "email": "example@gmail.com", 
            "password": "password2",
        }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(usr2), content_type='application/json')        
        self.assertEqual(response.status_code, 400)

    def test_register_user_with_missing_fields(self):
        usr = {
            "first_name": "Isaac",
            "email": "isaac@gmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",\
            data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_register_user_with_empty_fields(self):
        usr = {
            "first_name": "Allan",
            "last_name": "Obore",
            "email": "obore@gmail.com", 
            "password": "",
        }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_register_user_with_invalid_email(self):
        usr = {
            "first_name": "Goodluck",
            "last_name": "Obasanjo",
            "email": "obasgmailcom", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_login(self):
        user_logins = {
            "email": "example@gmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/login",\
        data=json.dumps(user_logins), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_with_wrong_password(self):
        user = {
            "first_name": "Goodluck",
            "last_name": "Obasanjo",
            "email": "example@gmail.com", 
            "password": "password",
        }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(user), content_type='application/json')
        user_logins = {
            "email": "example@gmail.com", 
            "password": "pword",
        }
        response = self.app.post("/api/v1/auth/login",\
            data=json.dumps(user_logins), content_type='application/json')
        self.assertEqual(response.status_code, 401)



    def test_get_all_users(self):
        usr1 = {
            "first_name": "Omar",
            "last_name": "Bashir",
            "email": "omar@gmail.com", 
            "password": "password22",
        }
        USERS.append(usr1)
        usr2 = {
            "first_name": "Riek",
            "last_name": "Machar",
            "email": "riek@gmail.com", 
            "password": "password22",
        }
        USERS.append(usr2)
        response = self.app.get('/api/v1/users', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    

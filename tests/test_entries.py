import unittest
import json
from tests.base import BaseTestCase

entry = entry = {
            'title': 'Go to Jinja',
            'description': 'Today am going cycling'
        }

class EntriesApiTestCase(BaseTestCase):
    def create_user(self):
        user = {
            "first_name": "Alex",
            "last_name": "Fergurson",
            "email": "alexf@gmail.com", 
            "password": "password",
            }
        response = self.app.post("/api/v1/auth/signup",\
        data=json.dumps(user), content_type='application/json')
        print(response)

    def test_add_an_entry(self):
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 201)


    # def test_get_an_entry(self):
    #     self.app.post("/api/v1/entries",\
    #     data = json.dumps(entry), content_type='application/json')
    #     response = self.app.get('/api/v1/entries/1', headers = self.header, content_type = 'application/json')
    #     self.assertEqual(response.status_code, 200)


    def test_add_entry_with_missing_fields(self):
        entry1 = {
            'description': 'This night is for coding'
        }
        response = self.app.post("/api/v1/entries",\
        data = json.dumps(entry1), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_add_entry_with_title_less_than_4_characters(self):
        entry = {
            'title': ' Go',
            'description': 'To the Beach'
        }
        response = self.app.post("/api/v1/entries",\
        data = json.dumps(entry), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_add_entry_with_description_less_than_6_characters(self):
        entry = {
            'title': ' Going to church',
            'description': 'Today'
        }
        response = self.app.post("/api/v1/entries",\
        data = json.dumps(entry), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_an_entry_not_in_list(self):
        entry = {
            'title': ' Visit a Cinema',
            'description': 'Go to Cineplex'
        }
        self.app.post("/api/v1/entries",\
        data = json.dumps(entry), content_type='application/json')
        response = self.app.get('/api/v1/entries/10', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 404)


    # def test_delete_entry(self):  
    #     user = {
    #         "first_name": "Alex",
    #         "last_name": "Fergurson",
    #         "email": "alexf@gmail.com", 
    #         "password": "password",
    #         }
    #     response = self.app.post("/api/v1/auth/signup",\
    #     data=json.dumps(user), headers = self.header, content_type='application/json')
    #     self.app.post("/api/v1/entries",\
    #     data = json.dumps(entry), headers = self.header, content_type='application/json')      
    #     response = self.app.delete('/api/v1/entries/1', headers = self.header, content_type = 'application/json')
    #     self.assertEqual(response.status_code, 200)

    def test_get_all_entries(self):
        response = self.app.get('/api/v1/entries', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)




    

    



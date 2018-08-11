import unittest
import json
from tests.base import BaseTestCase

entry = {
            'title': 'Go to Jinja',
            'description': 'Today am going cycling'
        }

user = {
            "first_name": "Alex",
            "last_name": "Fergurson",
            "email": "alexf@gmail.com", 
            "password": "password",
            }

class EntriesApiTestCase(BaseTestCase):
    
    def create_test_user(self):
        self.app.post("/api/v1/auth/signup",
        data=json.dumps(user), content_type='application/json')


    def create_test_entry(self):
        self.create_test_user()
        self.app.post("/api/v1/entries",
        data = json.dumps(entry), headers = self.header, content_type='application/json')
      

    def test_add_an_entry(self):
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_an_entry_without_token(self):
        self.create_test_user()
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry), content_type='application/json')
        self.assertEqual(response.status_code, 500)


    def test_add_entry_with_missing_title(self):
        self.create_test_user()
        entry1 = {
            'description': 'This night is for coding'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry1), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_missing_description(self):
        self.create_test_user()
        entry1 = {
            'title': 'Chalenge four'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry1), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_existing_title(self):
        self.create_test_entry()
        entry1 = {
            'title': 'Go to Jinja',
            'description': 'For honeymoon'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry1), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_add_entry_with_title_less_than_4_characters(self):
        ent = {
            'title': ' Go',
            'description': 'To the Beach'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(ent), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_add_entry_with_description_less_than_4_characters(self):
        entry = {
            'title': ' Going to church',
            'description': 'Now'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_get_all_entries(self):
        response = self.app.get('/api/v1/entries', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_a_single_entry_not(self):
        self.create_test_entry()
        response = self.app.get('/api/v1/entries/1', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_get_an_entry_not_in_list(self):
        response = self.app.get('/api/v1/entries/10', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_an_entry(self):
        self.create_test_entry()
        response = self.app.delete('/api/v1/entries/1', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_an_entry_that_does_not_exist(self):
        self.create_test_user()
        response = self.app.delete('/api/v1/entries/1', headers = self.header, content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    def test_edit_an_entry(self):
        self.create_test_entry()
        edit_details = {
            'description': 'For honeymoon'
        }
        response = self.app.put("/api/v1/entries/1",
        data = json.dumps(edit_details), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_edit_an_entry_with_invalid_description(self):
        self.create_test_entry()
        edit_details = {
            'description': 'For'
        }
        response = self.app.put("/api/v1/entries/1",
        data = json.dumps(edit_details), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_edit_an_entry_that_does_not_exist(self):
        self.create_test_user()
        edit_details = {
            'description': 'For'
        }
        response = self.app.put("/api/v1/entries/1",
        data = json.dumps(edit_details), headers = self.header, content_type='application/json')
        self.assertEqual(response.status_code, 404)
    
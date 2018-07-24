import unittest
import json
from app import app
from app.api.entries_resource import entries_list


class EntriesApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_an_entry(self):
        entry = {
            'title': 'Go for a meeting',
            'description': 'Meeting with investors from China'
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def test_get_all_entries(self):
        response = self.app.get('/api/v1/entries', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_add_entry_with_duplicated_title(self):
        entry1 = {
            'title': 'Go to Jinja',
            'description': 'Today am going cycling'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry1), content_type='application/json')
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry1), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_add_entry_with_empty_fields(self):
        entry1 = {
            'title': '',
            'description': 'I love cycling'
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry1), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_title_less_than_4_characters(self):
        entry = {
            'title': ' Go',
            'description': 'To the Beach'
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_description_less_than_6_characters(self):
        entry = {
            'title': ' Going to church',
            'description': 'Today'
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_entry(self):  
        entry = {
            'title': ' Live band',
            'description': 'At Kyadondo'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')      
        response = self.app.delete('/api/v1/entries/1', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        
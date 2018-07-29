import unittest
import json
from app import app
from app.api.entries_resource import ENTRIES


class EntriesApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        del ENTRIES[:]


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


    def test_add_entry_with_empty_title(self):
        entry1 = {
            'title': '',
            'description': 'I love cycling'
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry1), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_empty_description(self):
        entry1 = {
            'title': 'Rowing',
            'description': ''
        }
        response = self.app.post("/api/v1/entries",\
        data=json.dumps(entry1), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_entry_with_missing_fields(self):
        entry1 = {
            'description': 'This night'
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

    
    
    def test_edit_entry(self):
        entry = {
            'title': 'Swimming',
            'description': 'In Munyonyo'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        new_entry = {
            'title': 'Hunting',
            'description': 'In the park'
        }        
        response = self.app.put("/api/v1/entries/1",\
        data=json.dumps(new_entry), content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_edit_entry_that_does_not_exist(self):
        entry = {
            'title': 'Swimming',
            'description': 'In Munyonyo'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        new_entry = {
            'title': 'Hunting',
            'description': 'In the park'
        }        
        response = self.app.put("/api/v1/entries/10",\
        data=json.dumps(new_entry), content_type='application/json')
        self.assertEqual(response.status_code, 404)       


    def test_get_an_entry(self):
        entry = {
            'title': ' Visit a Cinema',
            'description': 'Go to Cineplex'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        response = self.app.get('/api/v1/entries/1', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_an_entry_not_in_list(self):
        entry = {
            'title': ' Visit a Cinema',
            'description': 'Go to Cineplex'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')
        response = self.app.get('/api/v1/entries/10', content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    
    def test_delete_entry(self):  
        entry = {
            'title': ' Live band',
            'description': 'At Kyadondo'
        }
        self.app.post("/api/v1/entries",\
        data=json.dumps(entry), content_type='application/json')      
        response = self.app.delete('/api/v1/entries/1', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
                
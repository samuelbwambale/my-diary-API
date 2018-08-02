import unittest
import json
from tests.base import BaseTestCase


class EntriesApiTestCase(BaseTestCase):

    def test_add_an_entry(self):
        pass 
        """ entry = {
            'title': 'Go to Jinja',
            'description': 'Today am going cycling'
        }
        response = self.app.post("/api/v1/entries",
        data = json.dumps(entry), headers = self.headers, content_type='application/json')
        self.assertEqual(response.status_code, 201)
 """
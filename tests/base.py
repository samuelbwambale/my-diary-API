import unittest
from app import app
from app.api.resources.entries_resource import ENTRIES
from app.api.resources.users_resource import USERS


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        del ENTRIES[:]
        del USERS[:]

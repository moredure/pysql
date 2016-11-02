import os
import pysql
import unittest
import tempfile

class PySqlTestCase(unittest.TestCase):

    def setUp(self):
        pysql.app.config['TESTING'] = True
        self.app = pysql.app.test_client()

    def home_test(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def user_test(self):
        rv = self.app.get('/users/1')
        assert rv.status_code == 200

    def sql_injection_test(self):
        payload = "' or 1=1 --"
        rv = self.app.get('/users/' + payload)
        assert b'\' or 1=1 --' in rv.data
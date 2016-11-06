import os
import pysql
import unittest
import tempfile

class PySqlTestCase(unittest.TestCase):

    def setUp(self):
        pysql.app.config['TESTING'] = True
        self.app = pysql.app.test_client()

    def logout_route_test(self):
        rv = self.app.get('/logout', follow_redirects=True)
        assert rv.status_code == 200

    def join_route_test(self):
        rv = self.app.get('/join')
        assert rv.status_code == 200

    def login_route_test(self):
        rv = self.app.get('/login')
        assert rv.status_code == 200

import os
import pysql
import unittest
import tempfile

class SqliTestCase(unittest.TestCase):

    def setUp(self):
        pysql.app.config['TESTING'] = True
        self.app = pysql.app.test_client()

    def sqli_test(self):
        rv = self.app.get('/users/\' or 1=1 --')
        assert b'\' or 1=1 --' in rv.data
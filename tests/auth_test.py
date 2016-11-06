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

    def join(self, creds):
        return self.app.post('/join', data=creds, follow_redirects=True) 

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def join_logout_login_logout_test(self):
        creds = dict(username='Mike Faraponov',login="mike1511",password="holly_crap", age=20)
        rv = self.join(creds)
        assert b'Search' in rv.data
        rv = self.logout()
        assert b'Login' in rv.data
        rv = self.login(creds['login'], creds['password'])
        assert b'Search' in rv.data
        rv = self.logout()
        assert b'Login' in rv.data
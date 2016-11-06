import os
from .helpers import auth, templated, deauth
from flask import Flask, redirect, request, session, url_for, render_template, g
from .db import get_db, init_db

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='pysql-s3cr37'
))

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db(app)
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['POST', 'GET'])
@auth
@templated('index.html')
def index():
    """Union SQL injection"""
    if request.method == 'POST':
        query = request.form['q']
        db = get_db()
        cur = db.execute("select username, login, age, id from users where username = '%s'" % (query))
        return dict(results=cur.fetchall())

@app.route('/logout')
@deauth
def logout():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
@templated('login.html')
def login():
    """Select SQL injection"""
    if request.method == 'POST':
        db = get_db()
        cur = db.execute("select id from users where login = '%s' and password = '%s' limit 1" % 
          (request.form['login'], request.form['password']))
        user = cur.fetchone()
        if user:
            session['id'] = user['id']
            return redirect(url_for('index'))
        return dict(error='Username of password is incorrect!')

@app.route('/join', methods=['POST', 'GET'])
@deauth
@templated('join.html')
def join():
    if request.method == 'POST':
        db = get_db()
        cur = db.execute('insert into users (login, username, password, age) values (?, ?, ?, ?)',
           [request.form['login'],
           request.form['username'],
           request.form['password'],
           request.form['age']])
        db.commit()
        session['id'] = cur.lastrowid
        return redirect(url_for('index'))

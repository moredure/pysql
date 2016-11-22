import os
from .helpers import auth, templated, deauth
from .db import get_db, init_db
from flask import Flask, redirect, request, session, url_for, render_template, g

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='pysql-s3cr37'
))

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db(app)
    get_db(app)
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'psql_db'):
        g.psql_db.close()

@app.route('/', methods=['POST', 'GET'])
@auth
@templated('index.html')
def index():
    """Union SQL injection"""
    if request.method == 'POST':
        cur = get_db().cursor()
        query = """select username, login, age, id
                from users
                where username like '%{0}%'
                """.format(request.form['q'])
        cur.execute(query)
        results = cur.fetchall()
        if not len(results):
            return dict(not_found=True)
        return dict(results=results)

@app.route('/logout')
@deauth
def logout():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
@templated('login.html')
def login():
    """Select SQL injection"""
    if request.method == 'POST':
        cur = get_db().cursor()
        login, passwd = request.form['login'], request.form['password']
        query = "select id "\
                "from users "\
                "where login = '{0}' and password = '{1}' limit 1"\
                .format(login, passwd)
        cur.execute(query)
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
        cur = db.cursor()
        query = """insert into users (login, username, password, age)
            values (%s, %s, %s, %s) returning id"""
        cur.execute(query, [request.form['login'],
           request.form['username'],
           request.form['password'],
           request.form['age']])
        db.commit()
        last_id = cur.fetchone()["id"]
        session['id'] = last_id
        return redirect(url_for('index'))

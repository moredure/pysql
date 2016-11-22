import os
import psycopg2
from urllib import parse
from psycopg2.extras import DictCursor
from flask import g

DBNAME_DEV = 'dbname=pysqldb user=postgres'

def connect_db():
    """Connects to the specific database."""
    try:
        parse.uses_netloc.append("postgres")
        url = parse(os.environ["DATABASE_URL"])
        with psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port) as conn:
            conn.cursor_factory = DictCursor
            return conn
    except:
        with psycopg2.connect(DBNAME_DEV) as conn:
            conn.cursor_factory = DictCursor
            return conn

def init_db(app):
    """Initializes the database."""
    with get_db() as db, \
        app.open_resource('schema.sql', mode='r') as schema, \
        app.open_resource('seed.sql', mode='r') as seed:
        with db.cursor() as cur:
            cur.execute(schema.read())
            cur.execute(seed.read())

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'psql_db'):
        g.psql_db = connect_db()
    return g.psql_db

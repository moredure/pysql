from flask import redirect, request, session, url_for, render_template
from functools import wraps
from .db import get_db

def auth(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        db = get_db()
        cur = db.execute('select * from users where id = ? limit 1', [session.get('id')])
        user = cur.fetchone()
        if not user:
            return redirect(url_for('login', next=request.url))
        return function(*args, **kwargs)
    return wrapper

def deauth(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        session.pop('id', None)
        return function(*args, **kwargs)
    return wrapper

def templated(template = None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
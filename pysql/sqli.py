from flask import Flask

app = Flask(__name__)

@app.route('/users/<id>')
def hello_world(id):
    return id
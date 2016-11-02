from flask import Flask

app = Flask(__name__)

@app.route('/users/<id>')
def user(id):
    app.logger.info(id)
    return id

@app.route('/')
def home():
    return 'home'

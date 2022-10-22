from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'goHello, World'

@app.route('/<name>')
def chicken(name):
    return f"Hello, {escape(name)}!"
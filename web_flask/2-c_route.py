#!/usr/bin/python3
"""Flask web application module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """'/' function"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb funtion"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """/c/<text> function"""
    return 'c {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

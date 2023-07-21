#!/usr/bin/python3
"""Flask web application module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """'/' function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb function"""
    return "HBNB"


if _name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

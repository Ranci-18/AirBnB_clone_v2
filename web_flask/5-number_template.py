#!/usr/bin/python3
"""Flask web application module"""
from flask import Flask, render_template


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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """diplay python text"""
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """display number only when n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """function displays html page only when n is an integer"""
    return render_template('./templates/5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

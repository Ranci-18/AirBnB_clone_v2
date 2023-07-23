#!/usr/bin/python3
"""Flask web application module"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown function"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """/states_list route function"""
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', Table="States",
                           items=dict_to_html)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

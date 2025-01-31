#!/usr/bin/python3
"""Flask web application module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown function"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_html():
    """/hbnb_filters route function"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', Table="States",
                           states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

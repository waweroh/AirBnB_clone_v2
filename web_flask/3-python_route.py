#!/usr/bin/python3
""" Start flask """
from email.policy import strict
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB when /hbnb is requested"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Shows text when txt when /c is requested"""
    return "C " + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text=str):
    """Shows text when /python is requested"""
    text = ("is cool")
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    """ My Main Function """
    app.run(host='0.0.0.0', port=5000)

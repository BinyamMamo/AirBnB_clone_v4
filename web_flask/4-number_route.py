#!/usr/bin/python3
"""uses flask to display text
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return the string "Hello HBNB!".
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return the string "HBNB"
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_(text):
    """
    The function hbnb takes a string as input and returns
       a modified version of the string by replacing
       underscores with spaces and adding a "C " prefix.

    Args:
      text: The text parameter is a string that
                represents a sentence or phrase.

    Returns:
      a string that starts with "C " and replaces all underscores
      in the input text with spaces.
    """
    return ("C " + text.replace("_", " "))


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_is_(text):
    """
    The function hbnb takes a string as input and returns
       a modified version of the string by replacing
       underscores with spaces and adding a "Python " prefix.

    Args:
      text: The text parameter is a string that
                represents a sentence or phrase.

    Returns:
      a string that starts with "Python " and replaces all underscores
      in the input text with spaces.
    """
    return ("Python " + text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_(n):
    """
    The function hbnb takes a string as input and returns
       a modified version of the string by replacing
       underscores with spaces and adding a "Python " prefix.

    Args:
      text: The text parameter is a string that
                represents a sentence or phrase.

    Returns:
      a string that starts with "Python " and replaces all underscores
      in the input text with spaces.
    """
    return (f"{n} is a number")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

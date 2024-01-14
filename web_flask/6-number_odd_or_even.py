#!/usr/bin/python3
"""uses flask to display text
"""
from flask import Flask, render_template, url_for


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
    This function takes an integer as input and
       returns a string indicating that the input is a number.

    Args:
      n: The parameter `n` is an integer that is passed as part of the URL.

    Returns:
      a string that says "{n} is a number", where {n} is
        the value of the variable n.
    """
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_is_(n):
    """The function returns a rendered template for a given number.
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    p = "even"
    if (n % 2):
        p = "odd"
    return render_template('6-number_odd_or_even.html', num=n, parity=p)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

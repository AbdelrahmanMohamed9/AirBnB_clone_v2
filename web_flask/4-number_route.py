#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Call with / route.. display HELLO HBNB '''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Call with /hbnb route.. display HBNB '''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' Call with /c/ route.. display C with text value '''
    return ('C %s' % text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' Call with /python/ route.. display Python with text value '''
    return ('Python %s' % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Call with /number/ route.. display <n> is a number '''
    return ('%d is a number' % n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

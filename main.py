import logging

from flask import Flask, error


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
 # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

@app.errorhandler(404)
def error404(error):
    return '<h3>Admit it,You Made a mistake.</h3><p>404</p>'

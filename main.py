import logging
from flask import Flask, redirect, render_template, request
from forms import RegistrationForm

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/signmein')


app.secret_key = 'you-will-never-guess'


@app.route('/signmein', methods=['GET', 'POST'])
def signmein():
    form = RegistrationForm()
    if request.method == 'POST':
        return redirect('/success')
    else:
        return render_template('signup.html', form=form)


@app.route('/success')
def success_signin():
    return 'Signin success'


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


@app.errorhandler(404)
def error404(error):
    return '<h3>Admit it,You Made a mistake.</h3><p>404</p>'


if __name__ == '__main__':
    app.run()

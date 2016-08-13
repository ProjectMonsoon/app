from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, validators, SubmitField, ValidationError


class RegistrationForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    test5 = BooleanField('I accept to all Terms & Conditions. ', [validators.DataRequired()])

    # class UploadPic(Form):
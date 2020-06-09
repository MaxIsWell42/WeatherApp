from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

class LocationForm(Form):
    city    = StringField('City', [validators.Length(min=4, max=25)])
    state   = StringField('State', [validators.Length(min=4, max=25)])
    mood    = StringField('Mood', [validators.Length(min=3, max=34)])
    submit = SubmitField('Enter')
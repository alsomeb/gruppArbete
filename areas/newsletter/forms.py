from email import message
from flask_wtf import FlaskForm
from wtforms import Form, validators,SelectField,FloatField,StringField
from wtforms.fields import IntegerField




class Newsletters(FlaskForm):
    email = StringField("Epost",[validators.Email()])
  
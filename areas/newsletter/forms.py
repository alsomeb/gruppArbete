from flask_wtf import FlaskForm
from wtforms import Form, validators,SelectField,FloatField,StringField,ValidationError
from wtforms.fields import IntegerField
from models import SignupsNewsletter


class Newsletters(FlaskForm):
    email = StringField("Epost",[validators.Email(), validators.Length(min=3, message="Check Email")])
    
    def validate_EmailAddress(self, EmailAddress):
        user = SignupsNewsletter.query.filter_by(email=EmailAddress.data).first()
        if user:
            currentEmail = user.email
            if EmailAddress.data == currentEmail:
                return EmailAddress.data
            else:
                raise ValidationError('Email Already Exist')
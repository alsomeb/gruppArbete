from flask_wtf import FlaskForm
from wtforms import Form, validators,SelectField,FloatField,StringField,ValidationError
from wtforms.fields import IntegerField, SubmitField
from website.models import SignupsNewsletter
from wtforms.widgets import TextArea


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


class EditNewsletter(FlaskForm):
    title = StringField("title", [validators.Length(min=1, max=255)])
    text = StringField('Text', [validators.Length(min=1, max=10000)], widget=TextArea())
    submit = SubmitField('Save changes')






class CreateNewsletter(FlaskForm):
    text = StringField("Text", [validators.Length(min=1, max=10000)])
    title = StringField('Title', [validators.Length(min=1, max=255)], widget=TextArea())
    submit = SubmitField('Save')







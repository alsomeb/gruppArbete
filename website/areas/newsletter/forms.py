from flask_wtf import FlaskForm
from wtforms import Form, validators,SelectField,FloatField,StringField,ValidationError
from wtforms.fields import IntegerField, SubmitField
from website.models import SignupsNewsletter, Newsletter
from wtforms.widgets import TextArea


class Newsletters(FlaskForm):
    email = StringField("Epost",[validators.Email(), validators.Length(min=3, message="Check Email")])
    
    def validate_EmailAddress(self, email):
        user = SignupsNewsletter.query.filter_by(email=email.data).first()
        if user:
            currentEmail = user.email
            if email.data == currentEmail:
                return email.data
            else:
                raise ValidationError('Email Already Exist')


class EditNewsletter(FlaskForm):
    title = StringField("title", [validators.Length(min=1, max=255)])
    text = StringField('Text', [validators.Length(min=1, max=10000)], widget=TextArea())
    submit = SubmitField('Save changes')


class CreateNewsletter(FlaskForm):
    title = StringField("Titel", [validators.Length(min=1, max=225), validators.DataRequired()])
    text = StringField('Text', [validators.Length(min=1, max=10000), validators.DataRequired()], widget=TextArea(), render_kw={"rows":10, "cols":50})
    submit = SubmitField('Lägg till nytt newsletter')

    def validate_title(self, title):
        letter = Newsletter.query.filter_by(title=title.data).first()
        if letter:
            raise ValidationError('Letter Title Already exists, choose another one...')

class ChooseNewsletter(FlaskForm):
    selectLetter = SelectField("Välj Nyhetsbrev", [validators.DataRequired()], choices=[])
    submit = SubmitField('Skicka')

    def __init__(self, letters=None): # <-- Så vi kan få in live alla brev i Selectfieldens lista // alex
        super().__init__()
        if letters:
            self.selectLetter.choices = [letter.title for letter in letters]








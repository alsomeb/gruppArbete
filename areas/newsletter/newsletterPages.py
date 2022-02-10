from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required
from areas.newsletter.forms import Newsletters
from areas.newsletter.services import validate_EmailAddress
from models import SignupsNewsletter, db

newsLetter = Blueprint('newsletter', __name__)

@newsLetter.route('/admin')
@roles_required("Admin")
def adminNewsletter() -> str:
  title = "Admin Panel"
  return render_template("newsletter/admin.html", title=title)

@newsLetter.route('/signUpConfirm', methods=["POST"])
def signUpConfirm() -> str:
  title = "Thank You"
  email = request.form.get('email')
  result = validate_EmailAddress(email)
  if result == False:
    addLetter = SignupsNewsletter()
    addLetter.email = email
    addLetter.isActive = True
    db.session.add(addLetter)
    db.session.commit()
    flash(f'{addLetter.email} was added to newsletters', 'success')
  if result == True:
    flash(f'Someone has already signed up with that email try again!','danger')
    return redirect(url_for('product.index'))
  return render_template("newsletter/thankYou.html", title=title, email=email)
from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required
from areas.newsletter.forms import Newsletters
from areas.newsletter.services import validate_EmailAddress
from models import SignupsNewsletter, db
from areas.newsletter.forms import EditNewsletter

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

@newsLetter.route('/admin/newsletters')
@roles_required("Admin")
def admin_Newsletter() -> str:
  title = "Newsletter Panel"

  list_of_newsletters = []


  return render_template("newsletter/admin_newsletters.html", title=title)

@newsLetter.route('/admin/newsletter/<id>')
@roles_required("Admin")
def newsletter(id) -> str:
  title = "Newsletter Panel"

  newsletter = '..'


  return render_template("newsletter/newsletter.html", title=title)


@newsLetter.route('/admin/newsletter/<id>/edit')
@roles_required("Admin")
def newsletter_edit(id) -> str:
  title = "Newsletter Panel"

  newsletter = '..'

  form = EditNewsletter(form.request)

  


  return render_template("newsletter/newsletter.html", title=title)


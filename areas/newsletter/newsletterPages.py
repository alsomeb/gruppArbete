from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required
from areas.newsletter.forms import Newsletters
from areas.newsletter.services import validate_EmailAddress
from models import SignupsNewsletter, Newsletter, db, NewsletterInfo
from areas.newsletter.forms import EditNewsletter

newsLetter = Blueprint('newsletter', __name__)

@newsLetter.route('/admin')
@roles_required("Admin")
def adminNewsletter() -> str:
  title = "Admin Panel"

  newsletters = db.session.query(SignupsNewsletter, NewsletterInfo).join(NewsletterInfo).all()
  return render_template("newsletter/admin.html", title=title, newsletters=newsletters)


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

  list_of_newsletters = Newsletter.query.all()

  return render_template("newsletter/admin_newsletters.html", title=title)

@newsLetter.route('/admin/newsletter/<id>')
@roles_required("Admin")
def newsletter(id) -> str:
  title = "Newsletter Panel"

  newsletter = Newsletter.query.filter(Newsletter.id == id).first()

  return render_template("newsletter/newsletter.html", title=title, newsletter=newsletter)


@newsLetter.route('/admin/newsletter/<id>/edit')
@roles_required("Admin")
def newsletter_edit(id) -> str:
  title = "Newsletter Panel"

  newsletter = Newsletter.query.filter(Newsletter.id == id).first()

  form = EditNewsletter(form.request)

  if request.method == 'GET':

    form.title.data = newsletter.title
    form.text.data = newsletter.text

    return render_template('newsletter_edit.html', 
        newsletter=newsletter, 
        form=form)

  if form.validate_on_submit():
    newsletter.title = form.title.data
    newsletter.text = form.text.data

    #db.session.commit()
    flash(f'Information updated for newsletter {newsletter.id}.', 'success')

  return render_template("newsletter/newsletter.html", title=title)


from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required
<<<<<<< HEAD
from areas.newsletter.forms import Newsletters
from areas.newsletter.services import validate_EmailAddress
from models import SignupsNewsletter, Newsletter, db, NewsletterInfo
from areas.newsletter.forms import EditNewsletter,CreateNewsletter
=======
from website.areas.newsletter.forms import Newsletters
from website.areas.newsletter.services import validate_EmailAddress
from website.models import SignupsNewsletter, Newsletter, db, NewsletterInfo
from website.areas.newsletter.forms import EditNewsletter
>>>>>>> f41b7b8242572569905f8fd5cd8e2c0d87c79105

newsLetter = Blueprint('newsletter', __name__)

@newsLetter.route('/admin')
@roles_required("Admin")
def adminNewsletter() -> str:
  title = "Admin Panel"
  newsletters = db.session.query(Newsletter).all()
  return render_template("newsletter/admin.html", title=title, newsletters=newsletters)

@newsLetter.route('/admin/newsletter/<id>', methods=["POST", "GET"])
@roles_required("Admin")
def listLettersById(id) -> str:
  currentLetter = Newsletter.query.filter(id == id).first()
  title = f"Showing letter {currentLetter.id}"
  letters = db.session.query(Newsletter, NewsletterInfo, SignupsNewsletter).select_from(Newsletter).join(NewsletterInfo).join(SignupsNewsletter).filter(Newsletter.id==id).all()
  newsLetterCount = db.session.query(Newsletter, NewsletterInfo).join(NewsletterInfo).filter(NewsletterInfo.letterId == id).count()
  return render_template("newsletter/list_newsletter.html", title=title, letters=letters, currentLetter=currentLetter, newsLetterCount=newsLetterCount)

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




@newsLetter.route("/new_newsleeter", methods=["GET", "POST"]) 
@roles_required("Admin")
def new_newsleeter():
    title = "Newsletter Panel"
    form = CreateNewsletter(request.form) 

    if request.method == "GET":
        return render_template('newsletter/new_newsleeter.html',form=form)

    if form.validate_on_submit():
        newsletterfronDB = Newsletters()
        newsletterfronDB.text = form.text.data
        newsletterfronDB.title = form.title.data 
        db.session.add(newsletterfronDB)
        db.session.commit()
        flash(f'Information saved for newsletter', 'success')
        return redirect(url_for('newsletter.new_newsleeter'))

    return render_template('newsletter/new_newsleeter.html',form=form,title=title)
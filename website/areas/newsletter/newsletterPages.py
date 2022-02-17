from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required
from website.areas.newsletter.forms import CreateNewsletter, ChooseNewsletter
from website.areas.newsletter.services import validate_EmailAddress, sendTestMail, sendNewsletters
from website.models import SignupsNewsletter, Newsletter, db, NewsletterInfo
from website.areas.newsletter.forms import EditNewsletter,CreateNewsletter

newsLetter = Blueprint('newsletter', __name__)

@newsLetter.route('/admin')
@roles_required("Admin")
def adminNewsletter() -> str:
  title = "Admin Panel"
  newsletters = db.session.query(Newsletter).all()
  # sendTestMail()
  return render_template("newsletter/admin.html", title=title, newsletters=newsletters)

@newsLetter.route('/admin/newsletter/<id>', methods=["POST", "GET"])
@roles_required("Admin")
def listLettersById(id) -> str:
  currentLetter = Newsletter.query.filter_by(id=id).first()
  title = f"{currentLetter.title}"
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


@newsLetter.route('/admin/newsletter/<id>/edit', methods = ["GET", "POST"])
@roles_required("Admin")
def newsletter_edit(id) -> str:
  title = "Newsletter Panel"

  newsletter = Newsletter.query.filter(Newsletter.id == id).first()

  form = EditNewsletter(request.form)

  if request.method == 'GET':

    form.title.data = newsletter.title
    form.text.data = newsletter.text

    return render_template('newsletter/newsletter_edit.html', 
        newsletter=newsletter, 
        form=form)

  if form.validate_on_submit():
    print('success')
    newsletter.title = form.title.data
    newsletter.text = form.text.data

    #db.session.commit()
    flash(f'Information updated for newsletter {newsletter.id}.', 'success')

  return redirect(url_for('newsletter.newsletter', id=id))




@newsLetter.route("/admin/newsletter/add", methods=["GET", "POST"]) 
@roles_required("Admin")
def new_newsletter():
    title = "Newsletter Panel"
    form = CreateNewsletter(request.form) 

    if request.method == "GET":
        return render_template('newsletter/new_newsletter.html',form=form, title=title)

    if form.validate_on_submit():
        newsletterfromDB = Newsletter()
        newsletterfromDB.text = form.text.data
        newsletterfromDB.title = form.title.data 
        db.session.add(newsletterfromDB)
        db.session.commit()
        flash(f'Nytt välkomstbrev skapat med titel {newsletterfromDB.title}', 'success')
        return redirect(url_for('newsletter.adminNewsletter'))

    return render_template('newsletter/new_newsletter.html',form=form,title=title)


@newsLetter.route("/admin/newsletter/send", methods=["GET", "POST"]) 
@roles_required("Admin")
def send_newsletter():
    title = "Skicka Newsletter"
    letters = Newsletter.query.all()
    form = ChooseNewsletter(letters=letters)
    if form.validate_on_submit():
        letterTitle = form.selectLetter.data
        getLetterObject = Newsletter.query.filter_by(title=letterTitle).first()
        sendNewsletters(getLetterObject)
        flash("Nyhetsbrev skickade till alla i databasen", "success")
        return redirect(url_for('newsletter.adminNewsletter'))

    return render_template('newsletter/send_newsletter.html',form=form,title=title)

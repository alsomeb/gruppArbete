from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required

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
  return render_template("newsletter/thankYou.html", title=title, email=email)
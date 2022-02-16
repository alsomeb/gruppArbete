from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required

siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact', methods=["POST","GET"])
def contact() -> str:
     if request.method == "POST":
          email = request.form.get('Email')
          flash(f"Du kommer bli kontaktad på: {email}", "success") # eller "danger" för röd error
          redirect(url_for("site.contact"))
     return render_template('site/contact.html')

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')

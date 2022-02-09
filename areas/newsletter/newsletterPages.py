from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required

newsLetter = Blueprint('newsletter', __name__)

@newsLetter.route('/admin')
def adminNewsletter() -> str:
  pass
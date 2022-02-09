from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_user import roles_accepted, roles_required

newsPaperBluePrint = Blueprint('newspaper', __name__)
from flask import Blueprint, request
from website.areas.newsletter.forms import Newsletters
from website.models import Newsletter, NewsletterInfo, SignupsNewsletter, db

apiBluePrint = Blueprint('api', __name__)


@apiBluePrint.route("api/newsletter/subscribe/<email>")
def subscribe(email:str):
  searchMail =  SignupsNewsletter.query.filter(email==email).filter(SignupsNewsletter.isActive==1).first()
  if searchMail:
    return {searchMail.email:"Subscribed Already"} # Dict already Json format 
  subMail = SignupsNewsletter()
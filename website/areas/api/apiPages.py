from flask import Blueprint, request
from website.models import Newsletter, NewsletterInfo, SignupsNewsletter, db
from website.areas.api.serverices import searchEmail

apiBluePrint = Blueprint('api', __name__)


@apiBluePrint.route("/api/newsletter/subscribe/<email>")
def subscribe(email:str):
  searchMail =  searchEmail(email)
  if searchMail:
    return {searchMail.email:"Subscribed Already"} # Dict already Json format 
  subMail = SignupsNewsletter()
  subMail.email = email
  subMail.isActive = True
  db.session.add(subMail)
  db.session.commit()
  return {"200":subMail.email}
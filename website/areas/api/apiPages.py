from datetime import datetime
from flask import Blueprint, jsonify, request
from website.models import Newsletter, NewsletterInfo, SignupsNewsletter, db
from website.areas.api.serverices import searchEmail, SubscriberApiModel, _mapSubscriberToApi
from datetime import datetime

apiBluePrint = Blueprint('api', __name__)


@apiBluePrint.route("/api/newsletter/subscribe/<email>")
def subscribe(email:str):
  searchMail =  searchEmail(email)

  if searchMail.isActive == False:
    subMail = SignupsNewsletter()
    subMail.email = email
    subMail.isActive = True
    db.session.add(subMail)
    db.session.commit()
    return {"200":subMail.email}
  return {searchMail.email:"Subscribed Already"} # Dict already Json format 


@apiBluePrint.route("/api/time")
def showCurrentTime()->datetime:
  return {"Current Time Right Now":datetime.utcnow()}


# http://127.0.0.1:5000/api/newsletter/listSubscribers?top=2&skip=2 example
@apiBluePrint.route("/api/newsletter/listSubscribers")
def listSubscribers():
  top = request.args.get("top", 2, type=int) #type int för vi vill säkställa att den inte blir string eller något annat
  skip = request.args.get("skip", type=int) 
  subscribersList = []
                                                                      #LIMIT = TOP / per page        #Skip = OFFSET, skippar 0,1 så 2 index
  subs = db.session.query(SignupsNewsletter).filter(SignupsNewsletter.isActive==True).limit(top).offset(skip).all()
  for subscriber in subs:
    sub = _mapSubscriberToApi(subscriber)
    subscribersList.append(sub)
  return jsonify([sub.__dict__ for sub in subscribersList])


@apiBluePrint.route("/api/newsletter/unsubscribe/<email>")
def unsubscribe(email):

  subscriber:SignupsNewsletter = SignupsNewsletter.query.filter_by(email=email).first()

  if subscriber == None:
    return {email:"is not subscribed"}

  if subscriber.isActive:
    subscriber.isActive = False
    db.session.commit()
    return{email:"unsubscribe lyckdes"}
  return{email:"is not subscribed"}  

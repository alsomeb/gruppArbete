from website.models import Newsletter, NewsletterInfo, SignupsNewsletter, db

class SubscriberApiModel():
  id = 0
  email = ""
  isActive = False

def _mapSubscriberToApi(subscriber)->SubscriberApiModel:
  subscriberApiModel = SubscriberApiModel()
  subscriberApiModel.id = subscriber.id
  subscriberApiModel.email = subscriber.email
  subscriberApiModel.isActive = subscriberApiModel.isActive
  return subscriberApiModel


def searchEmail(email:str)->SignupsNewsletter:
  email = SignupsNewsletter.query.filter_by(email=email).first()
  return email
from website.models import Newsletter, NewsletterInfo, SignupsNewsletter, db

def searchEmail(email:str)->SignupsNewsletter:
  email = SignupsNewsletter.query.filter_by(email=email).first()
  return email
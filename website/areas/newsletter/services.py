from website.models import SignupsNewsletter

def validate_EmailAddress(EmailAddress):
  customer = SignupsNewsletter.query.filter_by(email=EmailAddress).first()
  if customer:
    return True
  return False

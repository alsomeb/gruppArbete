from website.models import SignupsNewsletter
from flask_mail import Message
from website import mail
from website import create_app

def validate_EmailAddress(EmailAddress):
  customer = SignupsNewsletter.query.filter_by(email=EmailAddress).first()
  if customer:
    return True
  return False


def sendMail():
  app = create_app() # hämtar appen för att kunna skicka mail från flask
  with mail.connect() as conn:
    message = "hello from other side"
    subject = "Hej hopp din jävel"
    msg = Message(recipients=[f"test@testaren.se"], body=message, subject=subject)
    conn.send(msg)
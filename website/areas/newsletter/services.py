from website.models import Newsletter, SignupsNewsletter, NewsletterInfo, db
from flask_mail import Message
from website import mail
from website import create_app
from datetime import datetime

def validate_EmailAddress(EmailAddress):
  customer = SignupsNewsletter.query.filter_by(email=EmailAddress).first()
  if customer:
    return True
  return False


def sendTestMail():
  app = create_app() # hämtar appen för att kunna skicka mail från flask
  with mail.connect() as conn:
    message = "hello from other side"
    subject = "Hej hopp din jävel"
    msg = Message(recipients=[f"test@testaren.se"], body=message, subject=subject)
    conn.send(msg)


def sendNewsletters(letterObject:Newsletter):
  subscribers:list[SignupsNewsletter] = SignupsNewsletter.query.all()
  for sub in subscribers:
    with mail.connect() as conn:
      message = letterObject.text
      subject = letterObject.title
      msg = Message(recipients=[sub.email], body=message, subject=subject)
      conn.send(msg)
    # lägga till dem personer i table Newsletterinfo som blev skickade, så det är upd
    appendInfo = NewsletterInfo()
    appendInfo.dateSent = datetime.utcnow()
    appendInfo.letterId = letterObject.id
    appendInfo.receiverId = sub.id
    db.session.add(appendInfo)
    db.session.commit()

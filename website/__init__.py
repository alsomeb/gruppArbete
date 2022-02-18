from flask import Flask
from website.models import db,User, user_manager
from flask_migrate import Migrate
from website.config import ConfigDebug
from flask_mail import Mail

mail = Mail()

def create_app():
  app = Flask(__name__)
  app.config.from_object('website.config.ConfigDebug')

  db.app = app
  db.init_app(app)
  migrate = Migrate(app,db)
  user_manager.app = app
  user_manager.init_app(app,db,User)
  mail.init_app(app)

  from website.areas.newsletter.newsletterPages import newsLetter
  from website.areas.products.productPages import productBluePrint
  from website.areas.site.sitePages import siteBluePrint
  from website.areas.api.apiPages import apiBluePrint

  app.register_blueprint(siteBluePrint)
  app.register_blueprint(productBluePrint)
  app.register_blueprint(newsLetter)
  app.register_blueprint(apiBluePrint)

  if migrate:
    return app, migrate
  else:
    return app

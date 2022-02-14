from flask import Flask
from models import db, seedData, User, user_manager
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from areas.newsletter.newsletterPages import newsLetter
from flask_user import current_user

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
user_manager.app = app
user_manager.init_app(app,db,User)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)
app.register_blueprint(newsLetter)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
    app.run(debug=True)
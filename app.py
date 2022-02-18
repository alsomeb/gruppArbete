from website import create_app
from website.models import seedData

app, migrate = create_app()

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
    app.run()

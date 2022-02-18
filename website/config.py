class ConfigDebug():
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Ahmad123.@localhost/gruppUppgift'    # File-based SQL database
=======
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/gruppUppgift'    # File-based SQL database
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:sparven23@localhost/gruppUppgift'    # File-based SQL database
>>>>>>> abbefbb38c28a21832da6e084d46e25dade5b62e
    SECRET_KEY = 'SDFA11#'

 # Flask-Mail SMTP server settings
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 1025
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@steffe-shop.com'     
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"Steffe Shop" <noreply@steffe-shop.com>'

    # Flask-User settingsa
    USER_APP_NAME = "Steffe Shop"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email aution
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@steffe-shop.com"    

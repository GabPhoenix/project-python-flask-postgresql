from flask import Flask
from os import path

def app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'kjalksjddasd lkajsdjqiwueasndasd'

    from .views import views
    from .auth import auth
    from .models import User
    from .sendemail import send

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


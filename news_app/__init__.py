from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



from .config import Config

# instantiating db 
db = SQLAlchemy()

# importing blueprints 

from .models import User 
from .auth import auth
from .news import news


# creating the app 
def create_app():
    
    app = Flask(__name__)

    # loading configurations of app 
    app.config.from_object(Config)
    
    
    # db configuration of app 
    db.init_app(app)
    db.create_all(app=app)
    
    
    # login configurations
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # which view will handle the login part 
    login_manager.init_app(app)
    
    
    # define how to load the user.
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id) # it will call the get_id method and load user based on id returned 
    
    
    # register blueprints
    app.register_blueprint(auth) 
    app.register_blueprint(news) 
    
    return app 

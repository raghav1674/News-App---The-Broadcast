import os 

# configuration of the application
class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xc0\x83v\xf9\xa6%\xaa\xe3Q"g\x90\xd412\x8a'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///news_app.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
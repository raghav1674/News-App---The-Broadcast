from flask import Blueprint 

# news blueprint of our news_app 
news = Blueprint("news",__name__,template_folder='templates',static_folder='static')


from . import routes
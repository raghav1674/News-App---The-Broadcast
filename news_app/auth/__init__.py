from flask import Blueprint 

# auth blueprint for our news_app
auth = Blueprint("auth",__name__,template_folder='templates',static_folder='static')


from . import routes
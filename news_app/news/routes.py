from . import news
from  flask_login import login_required

# home route
@news.route("/index")
@news.route("/home")
@news.route("/")
@login_required
def index():
    return "Home Page"

# display news route
@news.route("/news")
@news.route("/news/<string:category>")
@login_required
def show_news(category="all"):
    return f"News Page - Category : {category}"

# add new  news route
@news.route("/add")
@news.route("/add-news")
@login_required
def add_news():
    return "Add news Page"


# contact us route
@news.route("/contact")
@news.route("/contact-us")
@news.route("/support")
@login_required
def contact():
    return "Contact Us Page"
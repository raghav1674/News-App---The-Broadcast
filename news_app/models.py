from werkzeug.security import check_password_hash,generate_password_hash

from news_app import db
from flask_login import UserMixin 


# many-to-many relation between category and news model
news_category = db.Table('news_category',
        db.Column('news_id',db.Integer,db.ForeignKey('news.news_id')),
        db.Column('category_name',db.String(29),db.ForeignKey('category.category_name')),
     )


# News table model
class News(db.Model):
    
    news_id = db.Column(db.Integer,primary_key=True)
    heading = db.Column(db.String(40),nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    # many to one relation with User model
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    
    
# category table model
class Category(db.Model):
    
    category_name = db.Column(db.String(30),primary_key=True)
    news = db.relationship('News',secondary = news_category)
    
# user table model
class User(db.Model,UserMixin):
    
    user_id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(60),nullable=False,unique=True)
    password = db.Column(db.String(130),nullable=False)
    is_admin = db.Column(db.Boolean,default=False)
    news  = db.relationship('News')
    
    # get the id of the user (need to return id as inheriting UserMixin)
    def get_id(self):
        return f'{self.user_id}'
    
    # store the password in hashed format
    def set_password(self,password):
        self.password = generate_password_hash(password,method='sha256')
        
    # check the password and stored hashed password
    def get_password(self,password):
        return check_password_hash(self.password,password)
    

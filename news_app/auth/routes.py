from flask import request,render_template,redirect,url_for
from  flask_login import login_user, logout_user,current_user,login_required

from . import auth 
from ..forms import LoginForm,RegisterForm
from ..models import User
from .. import db 


# login route
@auth.route("/sign-in",methods=['GET','POST'])
@auth.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # check if user exists or not 
            email = form.email.data
            password = form.password.data
         
            user = User.query.filter_by(email=email).first()
            
            if user and user.get_password(password):
                login_user(user,remember=True)
                return redirect(url_for('news.show_news'))
            # incorrect credentials
            return render_template('login.html',form=form)
    # not a post request   
    return render_template('login.html',form=form)



# register route
@auth.route("/sign-up",methods=['GET','POST'])
@auth.route("/register",methods=['GET','POST'])
def register():
    
    form = RegisterForm()
    
    if request.method == 'POST':
            if form.validate_on_submit():
                
                email = form.email.data
                password = form.password.data
                
                # create a new user
                new_user = User(email=email)
                new_user.set_password(password)
                
                # inserting to the db 
                db.session.add(new_user)
                db.session.commit()
                
                return redirect(url_for('auth.login'))
            
            # incorrect credentials
            return render_template('register.html',form=form)
    # not a post request   
    return render_template('register.html',form=form)



# logout route
@auth.route("/sign-out",methods=['GET','POST'])
@auth.route("/logout",methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
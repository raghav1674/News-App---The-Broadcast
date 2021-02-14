from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField,StringField,BooleanField,IntegerField,validators,ValidationError
from wtforms.validators import DataRequired,EqualTo,Email,Length

from .models import User  

# login forms
class LoginForm(FlaskForm):
    
    email = StringField(label="Email Address",validators=[DataRequired(),Email()])
    password = PasswordField(label="Password",validators=[DataRequired(),Length(min=4,max=12)])
    remember_me = BooleanField(label="Remember me")
    submit = SubmitField(label="Login")
    
        
# register form
class RegisterForm(FlaskForm):
    
    email = StringField(label="Email Address",validators=[DataRequired(),Email()])
    password = PasswordField(label="Password",validators=[DataRequired(),Length(min=4,max=12)])
    confirm_password = PasswordField(label="Confirm Password",validators=[EqualTo("password")])
    submit = SubmitField(label="Register")
   
    # check if email is already taken or not
    def validate_email(self,email):
        
        user = User.query.filter_by(email=email.data).first()
        # if user exists throw error
        if user:
            raise ValidationError("Email is already taken")
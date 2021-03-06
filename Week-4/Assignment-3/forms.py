from flask_wtf import FlaskForm
# from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)

from models import User
import pymysql


# def name_exists(form, field):
#     if User.select().where(User.username == field.data).exists():
#         raise ValidationError('User with that name already exists.')


def email_exists(form, field): ##
    # if User.select().where(User.email == field.data).exists():
    #     raise ValidationError('User with that email already exists.')
    db = pymysql.connect( host ="localhost",user ="root",password = "mypassword", database="assignment")
    cursor = db.cursor()
    result = cursor.execute("SELECT `email` FROM `user` WHERE `email`= %s", (field.data))
    if result > 0:
        raise ValidationError("Email already exists.") 

class RegisterForm(FlaskForm):
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
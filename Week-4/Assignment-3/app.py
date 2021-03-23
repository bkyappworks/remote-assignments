from flask import (Flask, g, render_template, flash, redirect, url_for,
                  abort)
from flask_bcrypt import Bcrypt     
from werkzeug.security import check_password_hash             
# from flask.ext.bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

import forms
import models
from models import User
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/', methods=('GET', 'POST'))
def index():
    return "Hello!"

@login_manager.user_loader 
def load_user(id):
    try:
        return models.User.get(models.User.id == id)
    except:
        return None


@app.before_request 
def before_request(): #logged_in = session.get('logged_in')
    """Connect to the database before each request."""
    g.db = models.db
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = forms.RegisterForm()
    
    if form.validate_on_submit():
        flash("Yay, you signed up!", "success")
        models.User.create_user(
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('member'))
    return render_template('register.html', form=form)

@app.route('/member', methods=('GET', 'POST'))
def member():
    return "Welcome!"


@app.route('/signin', methods=('GET', 'POST'))

def signin():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
        #user = models.User.select_user(form.email.data) # all success
        #user = models.User.select_user(models.User.email == form.email.data) # all mismatch
            email = models.User.select_user_email(email=form.email.data)
            password = models.User.select_user_pwd(password=form.password.data)
            if email:
                if password:
                    flash("Success")
                    # print(form) #<forms.LoginForm object at 0x7fc7b80091c0>
                    # print(form.email) #<input id="email" name="email" required type="text" value="aa@gmail.com">
                    return redirect(url_for('member'))
                elif password == None:
                    flash("Your email or password doesn't match!", "error")
            else:
                flash("Your email or password doesn't match!", "error")
        except:
            flash("Your email or password doesn't match!", "error")
    return render_template('login.html', form=form)



# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("You've been logged out! Come back soon!", "success")
#     return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    try:
        user = models.User.create_user(
            email = "test@gmail.com",
            password = "test123"
        )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)

    
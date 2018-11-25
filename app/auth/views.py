from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm, SignupForm
from ..import db
# from ..email import mail_message


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to Speed Pitching",
        #              "email/welcome_user", user.email, user=user)
        return redirect(url_for('auth.login'))
        title = "Create New Account"
    return render_template('auth/signup.html', signup_form=form)

from flask import render_template,request,redirect,url_for
from . import main 
# from .forms import
from ..models import User,Blog

#Views
@main.route('/')
def index():
    '''
    Retruns index page
    '''
    title = "BLOG HUB"
    return render_template('index.html', title = title)


@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

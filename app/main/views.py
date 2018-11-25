from flask import render_template,request,redirect,url_for
from . import main 
from .forms import 
from ..models import User

#Views
@main.route('/')
def index():
    '''
    Renders index page
    '''
    title = "Home"
    return render_template('index.html', title = title)
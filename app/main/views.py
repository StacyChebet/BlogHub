from flask import render_template,request,redirect,flash,url_for,abort
from ..models import User,Blog
from . import main 
from flask_login import login_required,current_user
from .forms import UpdateProfile,AddBlog,AddComment,AddSubscriber
from .. import db,photos
from ..email import mail_message
import datetime

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


@main.route('/user/<username>/update', methods=['GET', 'POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.profile = form.profile.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', username=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<username>/update/pic', methods=['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username=username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile', username=username))


@main.route('/upload/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = AddBlog()

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        content = form.content.data
        blog_photo = photos.save(request.files['photo'])
        path = f'photos/{filename}'

        new_blog = Blog(post_title=title, post_content=content,
                        photo_path=path, category=category, user=current_user)
        new_blog.save_blog()

    title = 'New Blog'
    return render_template('new_blog.html', title=title, blog_form=form)

from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile = db.Column(db.String)
    prof_pic = db.Column(db.String())
    blog = db.relationship("Blog", backref="user", lazy="dynamic")
    comments = db.relationship("Comment", backref='user',lazy='dynamic')
    pass_hash = db.Column(db.String(255))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('Stick to your lane!')

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)

    def get_blogs(self):
        user = User.query.filter_by(id=self.id).first()
        return user.blog


class Role(db.Model):
    '''
    Defines the roles
    '''
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Blog(db.Model):
    '''
    Pitch class to define pitch objects
    '''
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String)
    category = db.Column(db.String)
    blog = db.Column(db.String)
    blog_photo = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref = 'blog', lazy='dynamic')
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls, category):
        blogs = cls.query.filter_by(category=category).all()
        return blogs


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = cls.query.filter_by(blog_id=id).all()
        return comments

    @classmethod
    def delete_comment(cls, id):
        comment = cls.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

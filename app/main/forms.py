from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import Required,Email

class UpdateProfile(FlaskForm):
    profile = TextAreaField("Tell us about you", validators=[Required()])
    submit = SubmitField("Add")

class AddBlog(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('politics', 'Politics'), ('fashion', 'Fashion'), (
        'travel', 'Travel')], validators=[Required()])
    photo = FileField('Select an image', validators=[Required()])
    content = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Post')


class AddComment(FlaskForm):
    Name = StringField('Your Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Add your Comment')


    

    

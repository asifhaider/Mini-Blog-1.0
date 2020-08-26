# Flask Form based imports

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

# User based imports

from flask_login import current_user
from blogsite.models import User 

class LoginForm (FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm (FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Sorry, Your email has been registered with already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, Your username has been taken already!')

class UpdateUserForm (FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])

    picture = FileField('Update Profile Picture!', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Save Changes!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Sorry, Your email has been registered with already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, Your username has been taken already!')

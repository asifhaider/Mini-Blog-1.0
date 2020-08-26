####    IMPORTANT IMPORTS FOR DATABASE, LOGIN, DATE-TIME, PASSWORD SECURITY, USER FEATURES


from blogsite import db, login_manager 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

################ MODELS / PRIMARY DATA TABLES #################

# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User (db.Model, UserMixin):
    
    # table no 1: 

    __tablename__ = 'users'

    id = db.Column (db.Integer, primary_key=True)
    profile_image = db.Column (db.String(64),nullable=False, default='default_profile.png')
    email = db.Column (db.String(64), unique=True,index = True) # what does later two attributes mean?
    username = db.Column (db.String(64),unique=True,index = True)
    password_hash = db.Column (db.String(128))

    # 'posts' connects BlogPosts to a User Author
    
    posts = db.relationship('BlogPost', backref = 'author', lazy=True)

    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username: {self.username}"




class BlogPost(db.Model):

    # table no 2:

    users = db.relationship (User)

    id = db.Column (db.Integer, primary_key = True)

    # user_id connects User and BlogPost
    
    user_id = db.Column (db.Integer, db.ForeignKey('users.id'),nullable=False)
    date = db.Column (db.DateTime, nullable = False, default = datetime.utcnow)
    title = db.Column (db.String(140),nullable = False)
    text = db.Column (db.Text, nullable = True)

    def __init__(self,title,text,user_id):
        self.title=title
        self.text=text
        self.user_id=user_id
    
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.title}"


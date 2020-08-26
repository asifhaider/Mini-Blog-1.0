# module initializer for the main project directory, module named blogsite

# necessary imports for flask, database, migration, login tasks and functions

import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

from flask_login import LoginManager

##################################################

# initializing Flask app and secret key configuration
# this configuration needs to be taken care of while real deploying

app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

#############################################

### DATABASE SETUP 

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
Migrate(app,db)

######################## LOGIN CONFIGS #########################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

# BLUEPRINT CONFIGURATION 

from blogsite.core.views import core
from blogsite.users.views import users
from blogsite.blog_posts.views import blog_posts
from blogsite.error_pages.handlers import error_pages

#  REGISTERING THE BLUEPRINTS FOR THE APPS

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
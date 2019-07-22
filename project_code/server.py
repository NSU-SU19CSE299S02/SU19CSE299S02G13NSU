from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

##################################
#Connecting to the database and ORM as known sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from database import *

engine = create_engine('sqlite:///health.db')
Base.metadata.bind = engine
#Creates the session


session = scoped_session(sessionmaker(bind=engine))


@app.teardown_request
def remove_session(ex=None):
    session.remove()


##########################################









#============================
# Main Function
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

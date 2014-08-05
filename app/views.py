# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 13:13:01 2014

@author: pritishc
"""

from datetime import datetime
from nereid import flash, session, url_for, request, g, render_template, redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm, oid
from forms import LoginForm, EditForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [ # some posts
        {
            'author': {'nickname': 'John'},
            'body': 'This is a post.'            
        },
        {
            'author': {'nickname': 'Somebody'},
            'body': 'This is another post.'
        }
    ]
    
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session['remember_me'] = login_form.remember_me.data
        return oid.try_login(login_form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=login_form,
                           providers=app.config['OPENID_PROVIDERS'])
    
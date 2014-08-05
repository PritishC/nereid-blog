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


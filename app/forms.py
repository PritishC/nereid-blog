# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 10:16:59 2014

@author: pritishc
"""

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from trytond.transaction import Transaction

class LoginForm(Form):
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
    
class EditForm(Form):
    nickname = TextField('nickname', validators=[Required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    
    def __init__(self, nickname):
        self.original_nickname = nickname
    
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        table = User.__table__()
        cursor = Transaction.cursor()
        cursor.execute(*table.select(table.nickname, where=(table.nickname == self.nickname.data)))
        if cursor.fetchall() != None:
            self.nickname.errors.append('This nickname is already in use'.)
            return False
        return True
        
        
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 20:00:55 2014

@author: pritishc
"""

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool

ROLE_USER = 0
ROLE_ADMIN = 1

class User(ModelSQL, ModelView):
    """
    Defines a User of the blog.
    """
    _description = __doc__
    _name = "app.User"
    id = fields.Integer('ID')
    nickname = fields.Char('nickname')
    email = fields.Char('email')
    role = fields.Integer('role')
    
    @classmethod
    def default_role(cls):
        return ROLE_USER

Pool.register(User)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 20:00:55 2014

@author: pritishc
"""

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool

from hashlib import md5

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
    about_me = fields.Text('about_me')
    last_seen = fields.DateTime('last_seen')
    
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest()\
        + '?d=mm&s=' + str(size)
    
    @classmethod
    def default_role(cls):
        return ROLE_USER
        
class Post(ModelSQL, ModelView):
    """
    Defines a post on the blog.
    """
    _description = __doc__
    _name = "app.Post"
    

Pool.register(User)
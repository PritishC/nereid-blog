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

class User(ModelSQL):
    """
    Defines a User of the blog.
    """
    _description = __doc__
    _name = "app.user"
    id = fields.Integer('ID')
    nickname = fields.Char('nickname')
    email = fields.Char('email')
    role = fields.Integer('role')
    about_me = fields.Text('about_me')
    last_seen = fields.DateTime('last_seen')
    posts = fields.One2Many('app.post', 'user_id', 'Post')
    
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest()\
        + '?d=mm&s=' + str(size)
    
    @classmethod
    def default_role(cls):
        return ROLE_USER
        
    _sql_constraints = [('PrimaryKey', 'PRIMARY KEY(ID)', 'pk_error'),
                        ('UniqueNick', 'UNIQUE(nickname)', 'unique_error'),
                        ('UniqueEmail', 'UNIQUE(email)', 'unique_error')]
    
    _sql_error_messages = {'pk_error': 'This field is a primary key, it must\
    be specified!', 'unique_error': 'This field must be unique!'}
        
class Post(ModelSQL):
    """
    Defines a post on the blog.
    """
    _description = __doc__
    _name = "app.post"
    id = fields.Integer('ID')
    body = fields.Text('body')
    timestamp = fields.DateTime('timestamp')
    user_id = fields.Many2One('app.user', 'User')    
    
    _sql_constraints = [('PrimaryKey', 'PRIMARY KEY(ID)', 'pk_error')]    
    
    _sql_error_messages = {'pk_error': 'This field is a primary key, it must\
    be specified!'}

Pool.register(User)
Pool.register(Post)
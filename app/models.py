from .database import Base
from sqlalchemy import Column, String, Integer, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask.ext.login import UserMixin
from . import login_manager

class Permission:
    readable = 0x01
    writable = 0x02 
    administrate = 0x80


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    
    username = Column(String(64), nullable=False, index=True)
    password_hash = Column(String(128))
    permissions = Column(Integer, default=3)

    #meta
    create_at = Column(DateTime, default=datetime.now)
    last_seen = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<User %s>' % (self.username)

    @property
    def password(self):
        #raise AttributeError('Password is not readable')
        return self.pwd_hash

    @password.setter
    def password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pwd_hash, password)

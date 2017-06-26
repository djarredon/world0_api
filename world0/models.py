from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import backref, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from world0.database import Model


class User(Model):
    """
    User Model.
    """
    __tablename__ = 'user'
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)

    def __init__(self, username, email, password):
        self.email = email.lower()
        self.username = username.lower()
        self.set_password(password)

    def __repr__(self):
        return '<User %s>' % self.username

    def check_password(self, password):
        """Check a user's password (includes salt)."""
        return check_password_hash(self.password, password)

    def get_id(self):
        """Get the User id in unicode or ascii."""
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def set_password(self, password):
        """Using pbkdf2:sha512, hash `password`."""
        self.password = generate_password_hash(
            password=password,
            method='pbkdf2:sha512',
            salt_length=128
        )

    @classmethod
    def get_by_email_or_username(cls, email_or_username):
        return cls.query.filter(
            (cls.email==email_or_username) | (cls.username==email_or_username)
        ).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(cls.email==email).first()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter(cls.username==username).first()

    @property
    def is_authenticated(self):
        """Authenticaition check. Required for flask-login."""
        return True

    @property
    def is_active(self):
        """Active check. Required for flask-login."""
        return True

    @property
    def is_anonymous(self):
        """Anonimity check. Required for flask-login."""
        return False

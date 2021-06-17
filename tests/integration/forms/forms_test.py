from wtforms.validators import ValidationError
from tests.test_base import BaseTest, db
from market.__init__ import db
from market.models import User
from flask import request
from flask_login import current_user, AnonymousUserMixin
from market.forms import RegisterForm

class TestRegister(BaseTest):
    def test_valid_username(self):
        with self.app:
            self.app.post('/register', data=dict(
                username='jin', email_address='ethan@gmail.com',
                password1='1234567', password2='1234567'
            ), follow_redirects=True)
            class Username():
                data = 'jin'
            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_username(Username)
                self.assertEqual('Username already exists! Please try a different username', str(context.exception))
        
    def test_valid_email(self):
        with self.app:
            self.app.post('/register', data=dict(
                username='jin', email_address='ethan@gmail.com',
                password1='1234567', password2='1234567'
            ), follow_redirects=True)
            class Email():
                data = 'ethan@gmail.com'
            with self.assertRaises(ValidationError) as context:
                RegisterForm().validate_email_address(Email)
                self.assertEqual('Email Address already exists! Please try a different email address', str(context.exception))
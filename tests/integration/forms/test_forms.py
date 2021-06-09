from re import U

from werkzeug.wrappers import response
from market.tests.test_base import BaseTest, db
from flask_login import current_user, AnonymousUserMixin
from market.models import User
from flask import request

class SignUp(BaseTest):
    def test_username(self):
        with self.app:
            response = self.app.post('/sign_up',
                                    data=dict(username="ethanl", email_address="ethanl@gmail.com", password1=123456 , password2=123456),
                                    follow_redirects=True)
            user = db.session.query(User).filter_by(email='ethanl@gmail.com').first()
            self.assertTrue(user)                       
            self.assertIn(b'Account created', response.data)

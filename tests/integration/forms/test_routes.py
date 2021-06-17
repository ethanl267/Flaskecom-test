from tests.test_base import BaseTest,db
from market.models import User, Item
from flask import request
from flask_login import current_user

class TestRegister(BaseTest):
    
    def test_valid_register_success(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='Ethan', email_address='qwers@gmail.com',
                password1='python', password2='python'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Account created successfully! You are now logged in as Ethan', response.data)
           
    def test_invalid_registeration(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='Ethan', email_address='qwers@gmail.com',
                password1='python', password2='123456'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"There was an error with creating a user: ", response.data)
            
           

class TestLogin(BaseTest):
    def test_valid_login(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='Ethan', email_address='qwers@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            
            response = self.app.post('/login', data=dict(
                username='Ethan', password='python1'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Success! You are logged in as: Ethan', response.data)
            user = db.session.query(User).filter_by(username='Ethan').first()
            self.assertTrue(user)
            
    def test_invalid_login(self):
        with self.app:
            response = self.app.post('/login', data=dict(
                username='thor', password='123456'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Username and password are not match! Please try again', response.data)

class TestLogout(BaseTest):
    def test_(self):
        with self.app:
            response = self.app.post('/register', data=dict(
                username='Ethan', email_address='qwers@gmail.com',
                password1='python1', password2='python1'
            ), follow_redirects=True)
            
            response = self.app.post('/login', data=dict(
                username='Ethan', password='python1'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Success! You are logged in as: Ethan', response.data)
            user = db.session.query(User).filter_by(username='Ethan').first()
            self.assertTrue(user)

            #logs user out
            response = self.app.get('/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You have been logged out!', response.data)

            #redirects to logout page
            self.assertIn('/home', request.url)
            self.assertFalse(current_user.is_active)

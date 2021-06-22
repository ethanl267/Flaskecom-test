from re import U

import sys
sys.path.append("tests/test_base")
from tests.test_base import BaseTest
from market.models import User, Item
from market.__init__ import db

class TestModels(BaseTest):
    def test_user_crud(self):
        with self.app_context:
            user = User(username='qwerty', email_address='ethan@gmail.com', password_hash='password')
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNone(result)
            
            db.session.add(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNotNone(result)
            # assert note in db.session
            
            db.session.delete(user)
            db.session.commit()
            
            result = db.session.query(User).filter_by(username='qwerty').first()
            self.assertIsNone(result)
            
            
    def test_item_crud(self):
        with self.app_context:
            item = Item(name='paper', price=15, barcode='white', description='test')
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)
            
            db.session.add(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNotNone(result)
            # assert note in db.session
            
            db.session.delete(item)
            db.session.commit()
            
            result = db.session.query(Item).filter_by(name='paper').first()
            self.assertIsNone(result)

    def test_user_sell_method(self):
            with self.app:
                response = self.app.post('/register',
                data = dict(id=1, username='qwers', email_address='ethanl8@gmail.com', password1='1234567', password2='1234567', items=['testing'], follow_redirects=True))
                item = Item(name='testing', price=2000, barcode='testing', description='testing', owner=1)
                db.session.add(item)
                db.session.commit()

                user = db.session.query(User).filter_by(username='qwers').first()

                can_sell = user.can_sell(item)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(can_sell)


        
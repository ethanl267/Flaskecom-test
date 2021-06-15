from sys import path
path.append("C:/Users/Ragnar/Documents/FlaskEcom-master/market")

from unittest import TestCase
from market import models
from market.models import User, Item
from flask_bcrypt import bcrypt

class TestModels(TestCase):
    def test_user(self):
        user = models.User(username="qwers", email_address="qwers@gmail.com", password_hash=772245)
        self.assertEqual(user.username, "qwers")
        

class TestItems(TestCase):
    def test_item(self):
        item = models.Item(name="nike", barcode=234367, price="R200", description="from mr.price sports")
        self.assertEqual(item.name, "nike")


class TestModels(TestCase):
    def test_user(self):
        user = User(username='qwers', email_address='qwers@gmail.com', password_hash='password', budget=1200)
        
        self.assertEqual(user.username, 'qwers', "this the username")
        self.assertEqual(user.email_address, 'qwers@gmail.com', "testing email")
        self.assertEqual(user.password_hash, 'password', "test password")
        self.assertEqual(user.budget, 1200)
    
    def test_prettier_budget(self):
        budget = User(username='qwers', email_address='qwers@gmail.com', password_hash='password', budget=1200).prettier_budget
        self.assertEqual(budget, "1,200$")

    def test_password(self):
        user = User(username='qwers', email_address='qwers@gmail.com', password_hash='testing', budget=3000).password_hash

        self.assertEqual(user, 'testing')

    def test_password2(self):
        password = 'testing'
        pw_hash = bcrypt.generate_password_hash(password)

        self.assertTrue(pw_hash, 'testing')

    def test_password_correction(self):
        password = 'testing'
        pw_hash = bcrypt.generate_password_hash(password)

        fake = 'password'
        user = bcrypt.check_password_hash(pw_hash, fake)
        self.assertFalse(user)

    def test_can_purchase_method(self):
        user = User(username='qwers', email_address='ethan@gmail.com', password_hash='772245', budget=5000).can_purchase(Item(
            name='Phone', price=2000, barcode='234367', description='Model'
        ))

        self.assertTrue(user)

    def test_can_sell_method(self):
        item = User(username='qwers', email_address='ethan@gmail.com', password_hash='772245', items=['Phone']).can_sell(
            Item(name='Phone', price=2000, barcode='234367', description='Model')
        )
    def test_item_repr_method(self):
        item = Item(name='Phone', price=2000, barcode='234367', description='Model')

        new_item = item.__repr__()

        self.assertEqual(new_item, 'Item Phone')
    
    def test_item_buy_method(self):
        user = User(id=1, username='qwers', email_address='ethan@gmail.com', password_hash='772245', budget=5000)

        item = Item(name='Phone', price=2000, barcode='234367', description='Model', owner=1)

        can_buy = item.buy(user)

        db.session.commit()

        self.assertIsNone(can_buy)

    def test_item_sell_method(self):
        user = User(id=1, username='qwers', email_address='ethan@gmail.com', password_hash='772245', budget=5000)

        item = Item(name='Phone', price=2000, barcode='234367', description='Model', owner=1)

        can_sell = item.sell(user)

        db.session.commit()

        self.assertIsNone(can_sell)
from sys import path
path.append("C:/Users/Ragnar/Documents/FlaskEcom-master/market")

from unittest import TestCase
from market import models

class TestModels(TestCase):
    def test_user(self):
        user = models.User(username="qwers", email_address="qwers@gmail.com", password_hash=772245)
        self.assertEqual(user.username, "qwers")
        

class TestItems(TestCase):
    def test_item(self):
        item = models.Item(name="nike", barcode=234367, price="R200", description="from mr.price sports")
        self.assertEqual(item.name, "nike")

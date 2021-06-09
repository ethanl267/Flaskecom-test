from re import U
from tests.test_base import BaseTest, db
from market.models import User

class RegisterForm(BaseTest):
    def test_username(self):
        user = User()


from unittest import TestCase
from run import app 
from market import db 

class BaseTest(TestCase):
    # def setUpClass(cls):
    #     app.config['SQLALCHEMY_DATABAASE_URI'] = 'sqlite:///'
    #     app.config['WTF_CSRF_ENABLED'] = False
    #     with app.app_context():
    #         db.init_app(app)
            
    def setUp(self):
        app.config['SQLALCHEMY_DATABAASE_URI'] = 'sqlite:///'
        app.config['WTF_CSRF_ENABLED'] = False
        with app.app_context():
            db.create_all()
        self.app = app.test_client()
        self.app_content = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()


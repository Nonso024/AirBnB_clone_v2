#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os

class test_User(test_basemodel):
    """test class for user model"""

    def __init__(self, *args, **kwargs):
        """user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test acse for first name attribute """
        new = self.value()
        self.assertEqual(type(new.first_name), str) if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None)

    def test_last_name(self):
        """this test the user last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_email(self):
        """test case for email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """testing the password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

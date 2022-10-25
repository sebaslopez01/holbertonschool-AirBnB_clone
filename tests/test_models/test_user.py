#!/usr/bin/python3

"""

This module define a TestUser Class

"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    A TestUser Class
    """

    def test_email_attribute(self):
        user = User()
        user.email = 'example@gmail.com'

        self.assertEqual(user.email, 'example@gmail.com')

    def test_password_attribute(self):
        user = User()
        user.password = 'password'

        self.assertEqual(user.password, 'password')

    def test_first_name_attribute(self):
        user = User()
        user.first_name = 'Juan'

        self.assertEqual(user.first_name, 'Juan')

    def test_last_name_attribute(self):
        user = User()
        user.last_name = 'López'

        self.assertEqual(user.last_name, 'López')

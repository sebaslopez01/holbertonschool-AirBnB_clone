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
        User.email = 'example@gmail.com'

        self.assertEqual(User.email, 'example@gmail.com')

    def test_password_attribute(self):
        User.password = 'password'

        self.assertEqual(User.password, 'password')

    def test_first_name_attribute(self):
        User.first_name = 'Juan'

        self.assertEqual(User.first_name, 'Juan')

    def test_last_name_attribute(self):
        User.last_name = 'López'

        self.assertEqual(User.last_name, 'López')

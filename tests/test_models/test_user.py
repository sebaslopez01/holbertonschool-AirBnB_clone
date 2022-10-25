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
        self.assertEqual(User.email, '')

    def test_password_attribute(self):
        self.assertEqual(User.password, '')

    def test_first_name_attribute(self):
        self.assertEqual(User.first_name, '')

    def test_last_name_attribute(self):
        self.assertEqual(User.last_name, '')

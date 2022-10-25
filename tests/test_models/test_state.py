#!/usr/bin/python3

"""

This module define a TestState Class

"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    A TestState Class
    """

    def test_name_attribute(self):
        self.assertEqual(State.name, '')

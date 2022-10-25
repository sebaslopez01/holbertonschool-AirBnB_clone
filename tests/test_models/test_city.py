#!/usr/bin/python3

"""

This module define a TestCity Class

"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    A TestCity Class
    """

    def test_state_id_attribute(self):
        self.assertEqual(City.state_id, '')

    def test_name_attribute(self):
        self.assertEqual(City.name, '')

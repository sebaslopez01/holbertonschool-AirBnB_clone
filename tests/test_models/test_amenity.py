#!/usr/bin/python3

"""

This module define a TestAmenity Class

"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    A TestAmenity Class
    """

    def test_name_attribute(self):
        self.assertEqual(Amenity.name, '')

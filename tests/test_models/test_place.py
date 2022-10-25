#!/usr/bin/python3

"""

This module define a TestPlace Class

"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    A TestPlace Class
    """

    def test_city_id_attribute(self):
        self.assertEqual(Place.city_id, '')

    def test_user_id_attribute(self):
        self.assertEqual(Place.user_id, '')

    def test_name_attribute(self):
        self.assertEqual(Place.name, '')

    def test_description_attribute(self):
        self.assertEqual(Place.description, '')

    def test_number_rooms_attribute(self):
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        self.assertEqual(Place.number_bathrooms, 0)

    def test_price_by_night_attribute(self):
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_attribute(self):
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude_attribute(self):
        self.assertEqual(Place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        self.assertEqual(Place.amenity_ids, [])

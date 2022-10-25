#!/usr/bin/python3

"""

This module define a TestReview Class

"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    A TestReview Class
    """

    def test_place_id_attribute(self):
        self.assertEqual(Review.place_id, '')

    def test_user_id_attribute(self):
        self.assertEqual(Review.user_id, '')

    def test_text_attribute(self):
        self.assertEqual(Review.text, '')

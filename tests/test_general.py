#!/usr/bin/python3

"""

This module define a TestAmenity Class

"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestGeneral(unittest.TestCase):
    def test_email_attribute(self):
        self.assertEqual(User.email, '')

    def test_to_dict_method(self):
        bm = BaseModel()
        self.assertTrue(bm.to_dict())

    def test_id_attribute(self):
        bm = BaseModel()
        self.assertTrue(bm.id)

    def test_created_at_attribute(self):
        bm = BaseModel()
        self.assertTrue(bm.created_at)

    def test_sting_representation(self):
        bm = BaseModel()
        self.assertEqual(str(bm), f'[BaseModel] ({bm.id}) {bm.__dict__}')

#!/usr/bin/python3

"""

This module define a TestBaseModel Class

"""

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A TestBaseModel Class
    """

    def test_save_method(self):
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists('file.json'))
        os.remove('file.json')

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

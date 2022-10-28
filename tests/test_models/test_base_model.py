#!/usr/bin/python3

"""

This module define a TestBaseModel Class

"""

import unittest
import os
import json
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """
    A TestBaseModel Class
    """

    def test_save_method(self):
        models.storage.all().clear()
        bm = BaseModel()
        bm.save()
        with open('file.json', 'r') as f:
            json_obj = json.loads(f.read())
        self.assertDictEqual(json_obj, {f'BaseModel.{bm.id}': bm.to_dict()})
        
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

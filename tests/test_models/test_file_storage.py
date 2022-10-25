#!/usr/bin/python3

"""

This module define a TestFileStorage Class

"""

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    A TestFileStorage Class
    """

    def test_file_path_attribute(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, 'file.json')

    def test_objects_attribute(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, {})

    def test_all_method(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new_method(self):
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)

        self.assertDictEqual(storage.all(), {f'BaseModel.{bm.id}': bm})
        storage.all().clear()

    def test_save_method(self):
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        storage.save()

        with open('file.json', 'r') as f:
            json_obj = json.loads(f.read())

        self.assertDictEqual(json_obj, {f'BaseModel.{bm.id}': bm.to_dict()})

        storage.all().clear()
        os.remove('file.json')

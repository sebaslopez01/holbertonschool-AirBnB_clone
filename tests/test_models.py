#!/usr/bin/python3

"""

This module define test classes

"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class TestFileStorage(unittest.TestCase):
    def test_save_method(self):
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists('file.json'))
        os.remove('file.json')

    def test_id_attribute(self):
        bm = BaseModel()
        self.assertTrue(bm.id)

    def test_sting_representation(self):
        bm = BaseModel()
        self.assertEqual(str(bm), f'[BaseModel] ({bm.id} {bm.__dict__})')


class TestBaseModel(unittest.TestCase):
    pass


class TestUser(unittest.TestCase):
    pass


class TestPlace(unittest.TestCase):
    pass


class TestState(unittest.TestCase):
    pass


class TestCity(unittest.TestCase):
    pass


class TestReview(unittest.TestCase):
    pass


class TestAmenity(unittest.TestCase):
    pass

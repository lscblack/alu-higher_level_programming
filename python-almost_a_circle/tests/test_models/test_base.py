#!/usr/bin/python3
"""Test case"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class"""

    def test_basic(self):
        """Test basic func"""
        base = Base()
        base_1 = Base()
        base_89 = Base(89)
        self.assertEqual(base.id, 1)
        self.assertEqual(base_1.id, 2)
        self.assertEqual(base_89.id, 89)

    def test_to_json_string(self):
        """Test Func"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)

    def test_from_json_string(self):
        """Test Func"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(type(Base.from_json_string('[{"id": 89}]')), list)

    def test_save_to_file(self):
        """Test func"""
        Base._Base__nb_objects = 0

        Square.save_to_file(None)

        self.assertTrue(os.path.isfile("Square.json"))

        with open("Square.json") as fname:
            self.assertEqual(fname.read(), '[]')

        Square.save_to_file([])
        with open("Square.json") as fname:
            self.assertEqual(fname.read(), '[]')
            self.assertEqual(type(fname.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json") as fname:
            self.assertEqual(fname.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        
        with open("Rectangle.json") as fname:
            self.assertEqual(fname.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as fname:
            self.assertEqual(fname.read(), '[]')
            self.assertEqual(type(fname.read()), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as fname:
            self.assertEqual(fname.read(),
                             '[{"id": 1, "width": 1, '
                             '"height": 2, "x": 0, "y": 0}]')

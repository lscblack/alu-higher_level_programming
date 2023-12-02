#!/usr/bin/python3
"""Test Rectangle"""

import unittest
from io import StringIO
from unittest.mock import patch
import os

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for rectangle"""

    def test_instance(self):
        """Doc"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r4.id, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r11 = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r12 = Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r9 = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r13 = Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r14 = Rectangle(1, 2, 3, -4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(1, 2, 3, "4")

    def test_area(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.area(), 8)

    def test__str__(self):
        """Doc"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 2)
        with patch("sys.stdout", new=StringIO()) as seriously:
            print(r1)
            self.assertEqual(seriously.getvalue(),
                             "[Rectangle] (1) 0/0 - 4/2\n")

    def test_display(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        r2 = Rectangle(4, 2, 3)
        r3 = Rectangle(4, 2, 3, 2)
        with patch("sys.stdout", new=StringIO()) as seriously:
            r1.display()
            self.assertEqual(seriously.getvalue(),
                             "####\n####\n")
        with patch("sys.stdout", new=StringIO()) as seriously:
            r2.display()
            self.assertEqual(seriously.getvalue(),
                             "   ####\n   ####\n")
        with patch("sys.stdout", new=StringIO()) as seriously:
            r3.display()
            self.assertEqual(seriously.getvalue(),
                             "\n\n   ####\n   ####\n")

    def test_to_dictionary(self):
        """Doc"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 1, 'width': 4, 'height': 2, 'x': 0, 'y': 0})

    def test_update(self):
        """Doc"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 2)

        r1.update()
        self.assertEqual(r1.id, 1)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1.update(89, 1, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_create(self):
        """Doc"""

        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1 = Rectangle.create(**{'id': 89, 'width': 1,
                                 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_save_to_file(self):
        """Doc"""
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "width": 1, '
                             '"height": 2, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")
            self.assertEqual(type(file.read()), str)        

    def test_load_from_file(self):
        """Doc"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        from_file = Rectangle.load_from_file()
        self.assertEqual(type(from_file), list)
        self.assertEqual(from_file[0].width, 1)
        self.assertEqual(from_file[0].height, 2)

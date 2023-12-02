#!/usr/bin/python3
"""Test for Square"""

import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test for class Square"""

    def test_instance(self):
        """Test the functions in square"""
        s = Square(1)
        s1 = Square(1, 2)
        s2 = Square(1, 2, 3)
        s12 = Square(1, 0)
        s0 = Square(1, 2, 3, 4)

        self.assertEqual(s0.id, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s9 = Square(-1, 2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s10 = Square(1, -2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s11 = Square(0, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s13 = Square(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s4 = Square("1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5 = Square(1, "2")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s6 = Square(1, 2, "3")

    def test_area(self):
        """Test the functions in square"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

    def test__str__(self):
        """Test the functions in square"""
        Base._Base__nb_objects = 0
        s1 = Square(2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (1) 0/0 - 2\n")

    def test_display(self):
        """Test the functions in square"""
        s1 = Square(2)
        s2 = Square(2, 2, 3)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(),
                             "##\n##\n")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(),
                             "\n\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """Test the functions in square"""
        Base._Base__nb_objects = 0
        s1 = Square(4)
        self.assertEqual(s1.to_dictionary(),
                         {'id': 1, 'size': 4, 'x': 0, 'y': 0})

    def test_update(self):
        """Test the functions in square"""
        Base._Base__nb_objects = 0
        s1 = Square(2)
        s1.update()
        self.assertEqual(s1.id, 1)

        s1.update(89)
        self.assertEqual(s1.id, 89)

        s1.update(89, 1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

        s1.update(89, 1, 2)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

        s1.update(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s1.update(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

        s1.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s1.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_create(self):
        """Test the functions in square"""

        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s1 = Square.create(**{'id': 89, 'size': 1,
                              'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

        s1 = Square.create(**{'id': 89, 'size': 1,
                              'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_save_to_file(self):
        """Test the functions in square"""
        Base._Base__nb_objects = 0

        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')

        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")
            self.assertEqual(type(file.read()), str)

    def test_load_from_file(self):
        """Test the functions in square"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(2)])
        from_file = Square.load_from_file()
        self.assertEqual(type(from_file), list)
        self.assertEqual(from_file[0].size, 2)

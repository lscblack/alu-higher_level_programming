#!/usr/bin/python3
""" Unittest for Base Class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for Base class."""

    def setUp(self) -> None:
        """Set up the base class."""
        pass

    def tearDown(self) -> None:
        """Tear down the base class."""
        pass

    def test_id(self):
        """Test id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(98)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 98)
        self.assertEqual(b4.id, 3)

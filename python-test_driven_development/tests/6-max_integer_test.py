#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class MaxInteger(unittest.TestCase):
    def test_multiple_values(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([4,3]), 4)
        self.assertEqual(max_integer([5,6,2]), 6)
    
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)
    
    def test_one_element_list_negative(self):
        self.assertEqual(max_integer([-1]), -1)

if __name__ == '__main__':
    unittest.main()
    

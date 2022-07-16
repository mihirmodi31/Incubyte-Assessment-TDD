import unittest

from string_calculator import add_string_values

class TestStringCalculator(unittest.TestCase):

  def test_empty_string(self):
    self.assertEqual(add_string_values(""), 0)

  def test_comma(self):
    self.assertEqual(add_string_values("1"), 1)
    self.assertEqual(add_string_values("1,2"), 3)

  def test_newlines(self):
    self.assertEqual(add_string_values("1\n2,3"), 6)
    self.assertRaises(ValueError, add_string_values, "1,\n")

  def test_delimeter(self):
    self.assertEqual(add_string_values("//;\n1;2;3;4"), 10)
    self.assertEqual(add_string_values("//*\n1*2*3*4"), 10)
    self.assertRaises(ValueError, add_string_values, "//*\n1*\n")

  def test_negatives(self):
    self.assertRaises(ValueError, add_string_values ,"1,-2")

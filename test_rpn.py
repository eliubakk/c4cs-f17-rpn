import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)

	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)

	def test_divide(self):
		result = rpn.calculate('6 2 /')
		self.assertEqual(3, result)

	def test_multiply(self):
		result = rpn.calculate('5 6 *')
		self.assertEqual(30, result)

	def test_exponentiation(self):
		result = rpn.calculate('2 2 ^')
		self.assertEqual(4, result)
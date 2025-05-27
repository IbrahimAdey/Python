import to_do
from to_do_list import main
from unittest import TestCase

class Test_to_do(TestCase):
	def test_that_get_to_do_function_exists(self):
		
	
	def test_that_get_to_do_function_work_for_list_between_1_to_5(self):
		self.assertEqual(to_do.test_to_do(6), "invalid number")
		self.assertRaises(ValueError,to_do.test_to_do, 6)

	def test_that_get_to_do_function_raise_value_error_with_negative_value(self):
		self.assertRaises(ValueError, to_do.test_to_do, -1)

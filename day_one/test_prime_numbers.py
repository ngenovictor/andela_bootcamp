import unittest
from prime_numbers import prime_number_generator

class PrimeNumberGenerator(unittest.TestCase):
	def test_if_value_given_is_integer(self):
		self.assertEqual(prime_number_generator(0.5),"You should only provide integer values","Non-integer value provided")
	def test_if_value_is_less_than_2(self):
		self.assertEqual(prime_number_generator(0),"Use a value greater than 2","Value given less than 2")
		self.assertEqual(prime_number_generator(1),"Use a value greater than 2","Value given less than 2")
	def test_if_value_is_positive(self):
		self.assertEqual(prime_number_generator(-1),"Only provide positive numbers","Value given is negative")
	def test_if_result_is_list(self):
		self.assertEqual((type(prime_number_generator(50))),list,"Result Not List")
	def test_if_given_fucntion_works(self):
		self.assertEqual(prime_number_generator(20),[5, 7, 11, 13, 17, 19],"The function does not work")

if __name__ == "__main__":
	unittest.main()
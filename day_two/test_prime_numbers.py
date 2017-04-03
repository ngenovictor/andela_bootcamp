import unittest
from prime_numbers import prime_number_generator

class PrimeNumberGenerator(unittest.TestCase):
	def test_if_function_exists(self):
		self.assertEqual(prime_number_generator(),None,"Error")

if __name__ == "__main__":
	unittest.main()
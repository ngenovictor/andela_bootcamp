import unittest
from loan_calculator import loan_function

class LoanCalculator(unittest.TestCase):
	# test for loan_calculator
	def test_Loan_function_works(self):
		self.assertEqual(loan_function(100000,12,12), 112000,"Some Error")

if __name__ =="__main__":
	unittest.main()
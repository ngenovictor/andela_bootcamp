def loan_function(A,T,R):
	loan_payable = A+(A*(R/100.0)*(T/12.0))
	return loan_payable

print (loan_function(100000,12,12))
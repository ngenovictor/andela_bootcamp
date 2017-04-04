# A working function to generate prime numbers from 0 to n 
# with asymptotic analysis in your public Github Repo
def prime_number_generator(n):
	if type(n) != int:
		return "You should only provide integer values"
	elif n<0:
		return "Only provide positive numbers"
	elif n<2:
		return "Use a value greater than 2"
	else:
		for num in range(2,n):
			if num>1:
				for x in range(2,num):
					if (num%x==0):
						break
				else:	
					print (num)
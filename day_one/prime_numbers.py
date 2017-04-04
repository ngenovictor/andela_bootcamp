# A working function to generate prime numbers from 0 to n 
# with asymptotic analysis in your public Github Repo
def prime_number_generator(n):
	number_list = []
	if type(n) != int:
		return "You should only provide integer values"
	elif n<0:
		return "Only provide positive numbers"
	elif n<2:
		return "Use a value greater than 2"
	else:
		for num in range(2,n):
			number_list.append(num)
		for t in number_list:
			if t%2==0:
				number_list.remove(t)
		for t in number_list:
			if t%3==0:
				number_list.remove(t)
		number_list2 = number_list
		badnos=[]
		for num in number_list2:
			for nos in range (2,num):
				if num%nos==0:
					badnos.append(num)
					break
		for x in range(len(badnos)):
			if badnos[x] in number_list:
				number_list.remove(badnos[x])
					
		return number_list
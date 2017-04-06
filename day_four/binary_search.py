# First, you are to create a BinarySearch class, that inherits from the list class the following:
# the __init__() takes two integers as parameters, a and b. a is the length of the list to be created 
# and b is the step or difference between consecutive values. 
# It should also initialize an instance 
# variablelength`, that returns the number of elements in the array Once you are done, create another 
# method called search, it will take just one argument which is the value you are to find. The search 
# function should return a dictionary object, which contains count, the number of times you function 
# iterated to find the index of the number in question index, the index of the number in question 
# The search method should implement the binary search algorithm, each time you iterate, you should 
# increase the count, to test how efficient your implementation is.

class BinarySearch(list):
	"""
	a - length of list to be created
	b - step or diff btwn consecutive values
	variablelength - returns the number of elements in the array
	c - the value you are to find

	"""
	# def __init__(self, length, text):
	# 	super(BinarySearch, self).__init__()
	# 	for elem in range(1, length+1):
	# 		self.append(elem * text)
	# 	self.length = len(self)

	def __init__(self, a, b):
		super(BinarySearch,self).__init__()
		for t in range(1,a+1,b):
			self.append(t)
		self.length = len(self)

	def search(self,c):
		pass
print BinarySearch(20, 1).length
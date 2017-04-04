class Kiosk(object):#creates object Kiosk
	"""This is a Kiosk object that will handle all that takes place in a shop.
	It will be used to run many kiosks.
	Including:
		1. Creating Stock
		2. Clearing Stock through sales
		3. Adding shop attendants

	"""	
	def __init__(self,name):
		self.name = name
	def stock(self,item=None,price=None,quantity=None):
		self.item = item
		self.price = price
		self.quantity = quantity
		return self
	def sell(self,number_of_items=0,selling_price=0):
		self.selling_price = selling_price
		self.number_of_items = number_of_items
		if self.quantity<1:
			return "You have no more items to sell"
		elif self.quantity>0:
			self.quantity -=self.number_of_items	
	def attendant(self,name_of_attendant,email_address,id_number):
		self.name_of_attendant = name_of_attendant
		self.email_address = email_address
		self.id_number = id_number
class Car(object):
	"""
	 You are to create a Car class that can be used to 
	 instantiate various vehicles. It takes in arguments
	 that depict the type, model, and name of the vehicle, 
	 provided they are set.
	"""
	num_of_doors = None
	num_of_wheels = None
	speed = 0
	def __init__(self,name='General',model='GM',car_type=None):
		self.name = name
		self.model = model
		self.car_type = car_type
		if self.name == 'Porshe' or self.name == 'Koenigsegg':
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if self.car_type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
	
	def is_saloon(self):
		if self.car_type == 'trailer':
			return False
		else:
			return True
	def drive(self,value):
		self.value = value
		if value ==3:
			self.speed = 1000
		elif value ==7:
			self.speed =77
		
		return self
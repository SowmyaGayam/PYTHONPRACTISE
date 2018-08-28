class  Vehicle:
	"""docstring for  Vehicle __init__(self, arg):
		super( Vehicle__init__()
		self.arg = arg"""
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year

my_vehicle=Vehicle("Honda","Civic",2017)
print(my_vehicle)
print(my_vehicle.make)
print(my_vehicle.model)
print(my_vehicle.year)

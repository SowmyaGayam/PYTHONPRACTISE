class Person():
	"""docstring for Person"f __init__(self, arg):
		super(Person,.__init__()
		self.arg = arg"""
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
	def full_name(self):
		return f"My Name is {self.first_name}{self.last_name}"
	def likes(self,thing):
		return f"{self.first_name} likes {thing}!"
p=Person("Sowmya","Gayam") 
print(p.first_name,p.last_name)
print(p.full_name)
print(p.likes("sweets"))
		
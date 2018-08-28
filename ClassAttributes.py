##Difining attributes on a class

class Pet:
	"""docstring for Pet"f __init__(self, arg):
		super(Pet,.__init__()
		self.arg = arg"""
	allowed=("cat","dog","bird","lizard","rodent")
	def  __init__(self,kind,name):
		if kind not in self.allowed:
			raise ValueError(f"You can't have a {kind} as a pet here!")
		self.kind=kind
		self.name=name
		print(self.kind)
		print(self.name)

fluffy=Pet("cat","Fluffy")
fluffy2=Pet("dog","Fluffy")
fluffy3=Pet("rabit","Fluffy")
#print(fluffy)
			

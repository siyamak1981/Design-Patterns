class Pizza:
	def _init_(self,builder):
		self.garlic = builder.garlic
		
	def _str_(self):
		return 'this is a garlic from {}'.format(self.garlic)

	class PizzaBuilder():
		def _init_(self):
			self.garlic = False
	
		def add_garlic(self):
			self.garlic = True
			return self
		
		def build(self):
			return Pizza(self)
		
if __name__ == '__main__':
	pizza = Pizza.PizzaBuilder().add_garlic().build()
	print(pizza)
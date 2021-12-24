class N:
	def __init__(self):
		self.props = ["siyamak","saed"]
		
	def add(self,name):
		self.props.append(name)

	def read(self):
		print(f'my props is :{self.props}')

class B:
	def __init__(self):
		self.name = 'siyamak'
		
	def add(self):
		self.name=N()
		self.name.add('ali')
		self.name.read()
		print('hello {}...'.format(self.name))
		
		
x = B()
x.add()
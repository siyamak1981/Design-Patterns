# بعنوان یه پوسته و میانجی برای ابجکت ایتفاده میشود


class N:
	def foo(self):
		print('Study in college...')
	
class B:
	def __init__(self):
		self.name ='python'
	
	def bar(self):
		print(f'the cource is by {self.name}')
		self.name = N()
		self.name.foo()
	

x = B()
x.bar()
x.name = 'django'
x.bar()
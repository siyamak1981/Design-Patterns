


# یک الگوی طراحی خلاقانه است که به شما امکان می دهد خانواده های اشیاء مرتبط را بدون مشخص کردن کلاس های مشخص آنها تولید کنید.

# مشکلی که بدون Abstract Factory Method 
# با آن روبرو هستیم:
# تصور کنید می خواهید به یکی از دسته های نخبه
#  GeeksforGeeks
#  بپیوندید. بنابراین، شما به آنجا خواهید رفت و در مورد دوره های موجود، ساختار هزینه آنها، زمان بندی آنها و سایر موارد مهم سؤال خواهید کرد. آنها به سادگی به سیستم آنجا نگاه می کنند و تمام اطلاعات مورد نیاز را به شما می دهند. ساده به نظر می رسد؟ به توسعه دهندگان فکر کنید که چگونه سیستم را تا این حد سازماندهی می کنند و چگونه وب سایت آنها روان کننده است.

# توسعه دهندگان برای هر دوره کلاس های منحصر به فردی ایجاد می کنند که حاوی ویژگی های آن مانند ساختار هزینه، زمان بندی و موارد دیگر است. اما چگونه آنها را صدا می زنند و چگونه اشیاء خود را نمونه می کنند؟

# مشکل اینجا پیش می آید، فرض کنید ابتدا فقط 3-4 دوره در 
# GeeksforGeeks
#  موجود است، اما بعداً آنها 5 دوره جدید اضافه کردند.
# بنابراین، ما باید به صورت دستی اشیاء آنها را نمونه برداری کنیم که از نظر توسعه دهنده چیز خوبی نیست.

# Python Code for object
# oriented concepts without
# using the Abstract factory
# method in class

class DSA:

	""" Class for Data Structure and Algorithms """

	def price(self):
		return 11000

	def __str__(self):
		return "DSA"

class STL:

	"""Class for Standard Template Library"""

	def price(self):
		return 8000

	def __str__(self):
		return "STL"

class SDE:

	"""Class for Software Development Engineer"""

	def price(self):
		return 15000

	def __str__(self):
		return 'SDE'

# main method
if __name__ == "__main__":

	sde = SDE() # object for SDE class
	dsa = DSA() # object for DSA class
	stl = STL() # object for STL class

	print(f'Name of the course is {sde} and its price is {sde.price()}')
	print(f'Name of the course is {dsa} and its price is {dsa.price()}')
	print(f'Name of the course is {stl} and its price is {stl.price()}')



# راه حل آن جایگزینی فراخوانی ساده ساخت شی با فراخوانی به روش کارخانه انتزاعی ویژه است. در واقع، هیچ تفاوتی در ایجاد شی وجود نخواهد داشت، اما آنها در روش کارخانه فراخوانی می شوند.
# اکنون یک کلاس منحصر به فرد ایجاد می کنیم که نام آن Course_At_GFG است که تمام نمونه سازی آبجکت ها را به طور خودکار مدیریت می کند. اکنون، لازم نیست نگران این باشیم که چند دوره بعد از مدتی اضافه می کنیم



# Python Code for object
# oriented concepts using
# the abstract factory
# design pattern

import random

class Course_At_GFG:

	""" GeeksforGeeks portal for courses """

	def __init__(self, courses_factory = None):
		"""course factory is out abstract factory"""

		self.course_factory = courses_factory

	def show_course(self):

		"""creates and shows courses using the abstract factory"""

		course = self.course_factory()

		print(f'We have a course named {course}')
		print(f'its price is {course.Fee()}')


class DSA:

	"""Class for Data Structure and Algorithms"""

	def Fee(self):
		return 11000

	def __str__(self):
		return "DSA"

class STL:

	"""Class for Standard Template Library"""

	def Fee(self):
		return 8000

	def __str__(self):
		return "STL"

class SDE:

	"""Class for Software Development Engineer"""

	def Fee(self):
		return 15000

	def __str__(self):
		return 'SDE'

def random_course():

	"""A random class for choosing the course"""

	return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":

	course = Course_At_GFG(random_course)

	for i in range(5):
		course.show_course()

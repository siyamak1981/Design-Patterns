
# تصور کنید می خواهید به یکی از دسته های نخبه 
# GeeksforGeeks 
# بپیوندید. بنابراین، شما به آنجا می‌روید و در مورد ساختار هزینه،
#  زمان‌بندی موجود، و دسته‌هایی در مورد دوره‌ای که 
#  می‌خواهید به آن بپیوندید، سؤال خواهید کرد.
#   پس از مشاهده سیستم، آنها در مورد دوره ها، ساختار هزینه آنها،
#    زمان بندی موجود و دسته ها به شما خواهند گفت. 
#    خودشه! (نه! ما هنوز تمام نشده ایم زیرا توسعه دهندگان خوبی هستیم)

# هدف اصلی ما طراحی سیستم انعطاف پذیر، قابل اعتماد،
#  سازمان یافته و روان کننده است. کاری که توسعه دهندگان بی تجربه انجام خواهند
#   داد این است که یک کلاس جداگانه و منحصر به فرد برای هر دوره ارائه شده توسط 
# GeeksforGeeks 
# ایجاد می کنند.
#  سپس برای هر کلاس نمونه‌سازی شی جداگانه ایجاد می‌کنند،
#  هرچند که هر بار مورد نیاز نیست. مشکل اصلی زمانی ایجاد می‌شود که 
# GeeksforGeeks 
# دوره‌های جدیدی را شروع کند و توسعه‌دهندگان مجبور شوند
#  کلاس‌های جدیدی را نیز اضافه کنند، زیرا کد آنها چندان انعطاف‌پذیر نیست.

# بدون استفاده از 
# builder


# concrete course
class DSA():

	"""Class for Data Structures and Algorithms"""

	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

# concrete course
class SDE():

	"""Class for Software development Engineer"""

	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return "SDE"

# concrete course
class STL():

	"""class for Standard Template Library of C++"""

	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"


# main method
if __name__ == "__main__":

	sde = SDE() # object for SDE
	dsa = DSA() # object for DSA
	stl = STL() # object for STL

	print(f'Name of Course: {sde} and its Fee: {sde.fee}')
	print(f'Name of Course: {stl} and its Fee: {stl.fee}')
	print(f'Name of Course: {dsa} and its Fee: {dsa.fee}')


# راه حل با روش سازنده:
# محصول نهایی ما باید هر دوره ای از 
# GeeksforGeeks
#  باشد. ممکن است SDE، STL یا DSA باشد. ما باید قبل از انتخاب یک دوره خاص، مراحل زیادی را طی کنیم،
#  مانند یافتن جزئیات در مورد دوره ها، برنامه درسی،
#  ساختار شهریه، زمان بندی و دسته ها. در اینجا با استفاده از همین فرآیند می‌توانیم دوره‌های مختلف موجود در 
# GeeksforGeeks
#  را انتخاب کنیم. این مزیت استفاده از الگوی سازنده است.

# با استفاده از 
# builder
# Abstract course
class Course:

	def __init__(self):
		self.Fee()
		self.available_batches()

	def Fee(self):
		raise NotImplementedError

	def available_batches(self):
		raise NotImplementedError

	def __repr__(self):
		return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# concrete course
class DSA(Course):

	"""Class for Data Structures and Algorithms"""

	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

# concrete course
class SDE(Course):

	"""Class for Software Development Engineer"""

	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return "SDE"

# concrete course
class STL(Course):

	"""Class for Standard Template Library"""

	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"

# Complex Course
class ComplexCourse:

	def __repr__(self):
		return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course
class Complexcourse(ComplexCourse):

	def Fee(self):
		self.fee = 7000

	def available_batches(self):
		self.batches = 6

# construct course
def construct_course(cls):

	course = cls()
	course.Fee()
	course.available_batches()

	return course # return the course object

# main method
if __name__ == "__main__":

	dsa = DSA() # object for DSA course
	sde = SDE() # object for SDE course
	stl = STL() # object for STL course

	complex_course = construct_course(Complexcourse)
	print(complex_course)

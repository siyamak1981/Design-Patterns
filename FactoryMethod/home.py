class Dog:
	def _init_(self,name):
		self._name = name
		
def get_pet():
	pets=dict(dog=Dog("Mope"))
	return pets["dog"]
	
d= get_pet()
print(d._name)



# مثال دوم
class Dog:
	def _init_(self,speak):
		self.speak = "woof woff"
		
	def _str_(self):
		return self.speak
		
def foo():
	x =dict(dog = Dog('woof'))
	print(x["dog"])
z = foo()







# الگوی Factory
#  جزء الگوهای ایجاد اشیا می باشد. در این روش کدها مانند یک کارخانه عمل می
# کنند، کارخانه ای که وابسته به نیاز مشتری محصولی را در اختیار او می گذارد و ساخت شی محصول را
# به کالسهای پایین تر می سپارد و از آوردن کلمه new در کالس مشتری خودداری می کند. کالینت )
# استفاده کننده ( معموال شیء واقعی را ایجاد نمیکند بلکه با یک واسط و یا کالس انتزاعی
# )Abstract )در ارتباط است و کل مسئولیت ایجاد کالس واقعی را به Method Factory میسپارد.


# Factory Method
# یک الگوی طراحی خلاقانه است که به یک رابط یا کلاس اجازه می‌دهد یک شی بسازد، اما به کلاس‌های فرعی اجازه می‌دهد تصمیم بگیرند که کدام کلاس یا شی را نمونه‌سازی کنند. با استفاده از این روش  بهترین راه ها برای ایجاد یک شی را داریم.
#  در اینجا، اشیاء بدون ارائه منطق به مشتری ایجاد می شوند و برای ایجاد نوع جدید شی، مشتری از همان رابط مشترک استفاده می کند.

# تصور کنید استارت‌آپ خود را دارید که در بخش‌های مختلف کشور امکان اشتراک‌گذاری سواری را فراهم می‌کند. نسخه اولیه برنامه فقط اشتراک سواری دو چرخ را ارائه می دهد، اما با گذشت زمان، برنامه شما محبوب می شود و اکنون می خواهید سه و چهار چرخ سواری را نیز اضافه کنید.
# این یک خبر عالی است! اما در مورد توسعه دهندگان نرم افزار استارت آپ شما چطور؟ آنها باید کل کد را تغییر دهند، زیرا اکنون بیشتر بخش کد با کلاس Two-Wheeler همراه شده است و توسعه دهندگان باید تغییراتی را در کل پایگاه کد ایجاد کنند.
# پس از انجام تمام این تغییرات، یا توسعه دهندگان با کد درهم و برهم پایان می دهند یا با نامه استعفا.

# بیایید مفهوم را با یک مثال دیگر که مربوط به ترجمه ها و محلی سازی زبان های مختلف است، درک کنیم.
# فرض کنید برنامه‌ای ایجاد کرده‌ایم که هدف اصلی آن ترجمه یک زبان به زبان دیگر است و در حال حاضر برنامه ما فقط با 10 زبان کار می‌کند. اکنون برنامه ما به طور گسترده ای در بین مردم محبوب شده است، اما تقاضا به طور ناگهانی افزایش یافته است و شامل 5 زبان دیگر می شود.
# این یک خبر عالی است! فقط برای مالک نه برای توسعه دهندگان. آنها باید کل کد را تغییر دهند زیرا اکنون بیشتر بخش کد فقط با زبان های موجود همراه است و به همین دلیل است که توسعه دهندگان باید تغییراتی را در کل پایگاه کد ایجاد کنند که انجام آن واقعاً کار دشواری است.
# بیایید به کد مشکلی که ممکن است بدون استفاده از روش کارخانه با آن مواجه شویم نگاه کنیم.



# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, message):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):

		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

if __name__ == "__main__":

	# main method to call others
	f = FrenchLocalizer()
	e = EnglishLocalizer()
	s = SpanishLocalizer()

	# list of strings
	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))


# راه حل آن جایگزینی فراخوانی ساده ساخت شی با فراخوانی به روش کارخانه خاص است. در واقع، هیچ تفاوتی در ایجاد شی وجود نخواهد داشت، اما آنها در روش کارخانه فراخوانی می شوند.
# به عنوان مثال، کلاس های Two_Wheeler، Three_Wheeler و Four_wheeler ما باید رابط ridesharing را پیاده سازی کنند که متدی به نام ride را اعلام می کند. هر کلاس این روش را به صورت منحصر به فرد پیاده سازی می کند.




# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, message):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

def Factory(language ="English"):

	"""Factory Method"""
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))

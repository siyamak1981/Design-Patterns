# Flyweight pattern درباره ایجاد یک منبع (pool) از اشیاست که امکان به اشتراک گذاری اشیای ایجادشده و مصرف کمتر حافظه را فراهم می کند.
# Flyweight Design Pattern یکی از الگوهای ساخت یافته معرفی شده توسط GOF می باشد. این الگو با ایجاد منبعی از اشیا امکان اشتراک گذاری اشیای ایجاد شده را فراهم می کند و همچنین باعث کاهش مصرف حافظه می شود.
# بنابراین، این الگو دو کار انجام می دهد، از آنجا که این الگو اشیا را یکبار می سازد و در pool ذخیره می کند:
# 1. کارایی برنامه کاربردی را از جهت ایجاد شی افزایش می دهد، زیرا نیازی به ساختن شی با هر درخواست نمی باشد.
# 2. مصرف حافظه را کاهش می دهد، زیرا اشیای ساخته شده در حال حاضر در حافظه قرار دارند و به دلیل وجود pool شی جدیدی ساخته نمی شود.
# درنهایت، Flyweight Pattern برنامه های کاربردی را از نظر حافظه و سرعت پردازش کاراتر می کنند.


class ComplexCars(object):

	"""Separate class for Complex Cars"""

	def __init__(self):

		pass

	def cars(self, car_name):

		return "ComplexPattern[% s]" % (car_name)


class CarFamilies(object):

	"""dictionary to store ids of the car"""

	car_family = {}

	def __new__(cls, name, car_family_id):
		try:
			id = cls.car_family[car_family_id]
		except KeyError:
			id = object.__new__(cls)
			cls.car_family[car_family_id] = id
		return id

	def set_car_info(self, car_info):

		"""set the car information"""

		cg = ComplexCars()
		self.car_info = cg.cars(car_info)

	def get_car_info(self):

		"""return the car information"""

		return (self.car_info)



if __name__ == '__main__':
	car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
	car_family_objects = []
	for i in car_data:
		obj = CarFamilies(i[0], i[1])
		obj.set_car_info(i[2])
		car_family_objects.append(obj)

	"""similar id's says that they are same objects """

	for i in car_family_objects:
		print("id = " + str(id(i)))
		print(i.get_car_info())

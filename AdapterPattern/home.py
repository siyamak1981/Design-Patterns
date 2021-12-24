# یک آداپتور به دو رابط ناسازگار اجازه می‌دهد تا بتوانند با هم کار کنند. این یک تعریف کلی از مفهوم آداپتور است. ممکن است رابط ها ناسازگار باشند ولی قابلیت درونی آنها باید سازگار با نیاز باشد. الگوی طراحی آداپتور از طریق تبدیل رابط یک کلاس به رابط مورد انتظار توسط کلاینت، به کلاس‌های ناسازگار اجازه می‌دهد تا بتوانند از قابلیت‌های همدیگر استفاده کنند.

# مثلا سوکت های برق 3 شاخه رو حتما دیدین .
# این سوکت ها ممکنه در انگلستان به خوبی کار کنند ولی وقتی به ایران آورده می شود دیگر قابل استفاده نیست زیرا اکثر پریزهای برق داخل منازل از نوع 2 شاخه هستند پس باید یه آداپتور تهیه کنید تا این 3 شاخه را به 2 شاخه تبدیل کند و بتوان از آن استفاده کنید .

# چیزی که در ساخت آداپتور مهم است این است که شما لازم نیست رفتار شی اتون رو تغییر دهید .تنها چیزی که لازم است این است که آداپتوری ایجاد کنید که اون سوکت 3 شاخه را به 2 شاخه تبدیل کند



# Dog - Cycle
# human - Truck
# car - Car

class MotorCycle:

	"""Class for MotorCycle"""

	def __init__(self):
		self.name = "MotorCycle"

	def TwoWheeler(self):
		return "TwoWheeler"


class Truck:

	"""Class for Truck"""

	def __init__(self):
		self.name = "Truck"

	def EightWheeler(self):
		return "EightWheeler"


class Car:

	"""Class for Car"""

	def __init__(self):
		self.name = "Car"

	def FourWheeler(self):
		return "FourWheeler"

class Adapter:
	"""
	Adapts an object by replacing methods.
	Usage:
	motorCycle = MotorCycle()
	motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
	"""

	def __init__(self, obj, **adapted_methods):
		"""We set the adapted methods in the object's dict"""
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		"""All non-adapted calls are passed to the object"""
		return getattr(self.obj, attr)

	def original_dict(self):
		"""Print original object dict"""
		return self.obj.__dict__


""" main method """
if __name__ == "__main__":

	"""list to store objects"""
	objects = []
	motorCycle = MotorCycle()
	objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))

	truck = Truck()
	objects.append(Adapter(truck, wheels = truck.EightWheeler))

	car = Car()
	objects.append(Adapter(car, wheels = car.FourWheeler))

	for obj in objects:
		print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))





# تصور کنید در حال ایجاد برنامه ای هستید که داده های مربوط به انواع مختلف وسایل نقلیه موجود را نشان می دهد.
#  داده ها را از 
# API
#  سازمان های خودروهای مختلف در قالب XML می گیرد و سپس اطلاعات را نمایش می دهد.
# اما فرض کنید زمانی می خواهید برنامه خود را با یک الگوریتم یادگیری ماشینی ارتقا دهید که به زیبایی روی داده ها کار می کند و فقط داده های مهم را واکشی می کند. اما یک مشکل وجود دارد، فقط با فرمت JSON داده می گیرد.
# ایجاد تغییرات در الگوریتم یادگیری ماشین به طوری که داده ها را در قالب XML بگیرد، یک رویکرد واقعا ضعیف خواهد بود.



# # 
# برای حل مشکلی که در بالا تعریف کردیم، می‌توانیم از 
# Adapter Method
#  استفاده کنیم که با ایجاد یک شی
#  Adapter 
# کمک می‌کند.
# برای استفاده از یک آداپتور در کد ما:

# کلاینت باید با فراخوانی روشی روی آداپتور با استفاده از رابط هدف، درخواستی را به آداپتور ارائه دهد.
# با استفاده از رابط Adaptee، آداپتور باید آن درخواست را بر روی Adaptee ترجمه کند.
# نتیجه تماس مشتری دریافت می شود و او از حضور آداپتور بی اطلاع است.
# به طور کلی، الگوی طراحی فِساد زیرشاخۀ الگوهای طراحی Structural قرار می‌گیرد و استفاده از آن در شرایطی مؤثر واقع می‌شود که کدی پیچیده داشته باشیم که با چندین کلاس مختلف پیاده‌سازی شده است یا زمانی که یک کد به اصطلاح Legacy (قدیمی) داریم که ریفکتور کردن آن بسیار دشوار و زمان‌بر می‌باشد 


# تصور کنید ما یک ماشین لباسشویی داریم که می تواند لباس ها را بشویید، لباس ها را آبکشی کند و لباس ها را بچرخاند اما همه کارها را جداگانه انجام دهد. از آنجایی که کل سیستم کاملاً پیچیده است، باید پیچیدگی‌های زیرسیستم‌ها را انتزاع کنیم. ما به سیستمی نیاز داریم که بتواند کل کار را بدون مزاحمت یا دخالت ما خودکار کند.


"""Facade pattern with an example of WashingMachine"""

class Washing:
	'''Subsystem # 1'''

	def wash(self):
		print("Washing...")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("Rinsing...")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Spinning...")


class WashingMachine:
	'''Facade'''

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	washingMachine = WashingMachine()
	washingMachine.startWashing()

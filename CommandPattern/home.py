"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""
class Command(ABC):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver
	
	"""process method"""
	def process(self):
		pass

"""Class dedicated to Command Implementation"""
class CommandImplementation(Command):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver

	"""process method"""
	def process(self):
		self.receiver.perform_action()

"""Class dedicated to Receiver"""
class Receiver:
	
	"""perform-action method"""
	def perform_action(self):
		print('Action performed in receiver.')

"""Class dedicated to Invoker"""
class Invoker:
	
	"""command method"""
	def command(self, cmd):
		self.cmd = cmd

	"""execute method"""
	def execute(self):
		self.cmd.process()

	
"""create Receiver object"""
receiver = Receiver()
cmd = CommandImplementation(receiver)
invoker = Invoker()
invoker.command(cmd)
invoker.execute()


# Command Method
#  یک الگوی طراحی رفتاری است که یک درخواست را به عنوان یک شی کپسوله می کند،
#  در نتیجه امکان پارامترسازی مشتریان با درخواست های مختلف و صف بندی یا ثبت درخواست ها را فراهم می کند.
#  پارامتربندی اشیاء دیگر با درخواست های مختلف در قیاس ما به این معنی است که 
# دکمه ای که برای روشن کردن چراغ ها استفاده می شود می تواند بعداً
#  برای روشن کردن استریو یا شاید باز کردن درب گاراژ استفاده شود
# . این کمک می کند تا "فراخوانی یک روش بر روی یک شی" را به وضعیت شی کامل ارتقا دهد
# . اساساً، تمام اطلاعات مورد نیاز برای انجام یک عمل یا راه‌اندازی یک رویداد را کپسوله می‌کند.
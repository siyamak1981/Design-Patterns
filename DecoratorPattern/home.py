# تصور کنید ما با یک ابزار قالب‌بندی کار می‌کنیم که ویژگی‌هایی مانند 
# Bold the text و  Underlines the text
#  کردن متن را ارائه می‌دهد.
#  اما پس از مدتی، ابزارهای قالب‌بندی ما در بین مخاطبان هدف شهرت یافتند 
# و با گرفتن بازخورد دریافتیم که مخاطبان ما به ویژگی‌های
#  بیشتری در برنامه مانند ساخت متن و بسیاری از ویژگی‌های دیگر می‌خواهند.
# ساده به نظر می رسد؟ این کار آسانی نیست که این را اجرا کنیم
#  یا کلاس‌هایمان را برای افزودن قابلیت‌های بیشتر بدون ایجاد اختلال
#  (the Single Responsibility Principle)در کد مشتری موجود، گسترش دهیم، زیرا ما باید اصل مسئولیت واحد را حفظ کنیم
# راه حل چیست؟
# حال بیایید به راه حلی که برای اجتناب از چنین شرایطی باید توجه کنیم. 
# در ابتدا فقط 
# WrittenText 
# داریم اما باید فیلترهایی مانند 
#  ITALIC، UNDERLINE
#  را اعمال کنیم. بنابراین، ما برای هر تابع مانند
#  BoldWrapperClass، ItalicWrapperClass و UnderlineWrapperclass
#  wrapper کلاس‌های
#   جداگانه ایجاد می‌کنیم.


class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())


before_gfg = WrittenText("GeeksforGeeks")
after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

print("before :", before_gfg.render())
print("after :", after_gfg.render())

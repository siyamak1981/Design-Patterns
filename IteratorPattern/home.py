# زنجیره مسئولیت
# زنجیره مسئولیت یکی از الگوهای طراحی در پایتون است
#  که راهی را در اختیار ما می‌گذارد تا با استفاده از متدهای مختلف یک 
#  درخواست را اجرا کنیم، به طوری که هر کدام از آنها یک قسمت مشخص از 
#  درخواست را آدرس دهی نمایند. همانطور که می‌دانید یکی از بهترین اصول یک کد خوب،
#   رعایت اصل تک مسئولیتی است. به بیان دیگر
#   ، هر قسمت از کد، باید یک و تنها یک کار را انجام 
#   . این اصل به شکلی کاملا عمیق در این الگوی طراحی در پایتون، یکپارچه شده است
#  راهی برای دسترسی متوالی به عناصر ساختار داده پیچیده بدون تکرار آنها فراهم می کند.


#  یک روشی برای دسترسی مجموعه ای از اشیا هم جنس و پشت سر هم )مانند لیست
# پیوندی( است بدون آنکه درگیر جزییات )مانند نحوه اتصال اشیا به هم و ....( شویم.


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name :<6}: $ {self.price}"

class Menu:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def remove(self):
        return self.items.pop()

    def iterator(self):
        return MenuIterator(self.items)


class MenuIterator:
    def __init__(self, items):
        self.indx = 0
        self.items = items

    def has_next(self):
        return False if self.indx >= len(self.items) else True

    def next(self):
        item = self.items[self.indx]
        self.indx += 1
        return item

if __name__ == '__main__':
    i1 = FoodItem("Burger", 7)
    i2 = FoodItem("Pizza", 8)
    i3 = FoodItem("Coke", 5)

    menu = Menu()
    menu.add(i1)
    menu.add(i2)
    menu.add(i3)

    print("Displaying Menu:")
    iterator = menu.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)
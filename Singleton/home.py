# از هر متا کلاس فقط یکی بشه ابجکت ساخت واستفاده کرد

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwds) :
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
        

class DB(metaclass = Singleton):
    pass

x = DB()
y = DB()
print(x == y)
print(x is y)

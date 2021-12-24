import copy

class Proto:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        self._objects[name]
        
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "pezho"
        self.color = "red"
    def __str__(self):
        return "{}, {}".format(self.name, self.color)


c = Car()
p = Proto()
p.register("siyamak", c)
po = p.clone("siyamak")
print(po)

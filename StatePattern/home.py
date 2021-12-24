from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):
    @abstractmethod
    def handling(self):
        print("hello starting ...")
       


class ConceretStateOne(State):
    def __init__(self):
        self.radio = "radio"


    def handling(self):
        print("this is concereteone ..")
       


class ConceretStateTwo(State):
    def __init__(self):
        pass


    def handling(self):
        print("this is conceretetwo ...")
 
        

class Context(State):
    def __init__(self):
        pass
    
    def setstate(self, item):
        self.state = item
    
    def getstate(self):
        return self.state

    def handling(self):
        self.state.handling()


context = Context()
state1 = ConceretStateOne()
state2 = ConceretStateTwo()
context.setstate(state1)
context.handling()
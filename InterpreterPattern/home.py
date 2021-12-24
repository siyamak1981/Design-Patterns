class Abstract:
    def interpreter(self,context):
        print("this is test for does not display")
        raise ValueError("i dont need it")


class TerminalExpression(Abstract):
    def interpreter(self,context):
        print("hello i will do it ..")


class NonterminalExpression(Abstract):
    def interpreter(self,context):
        print("good bye i donot will do it")


class Context:
    def __init__(self,value):
        self.experssion = value
    
    def setexperssion(self, value):
        self.experssion = value

    def getexpersion(self):
        return self.value


contextObj = Context("slkdjvoisdfvv")
experssionList = []
experssionList.append(TerminalExpression())
experssionList.append(TerminalExpression())
experssionList.append(NonterminalExpression())
experssionList.append(NonterminalExpression())
for i in experssionList:
    i.interpreter(contextObj)
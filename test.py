from abc import ABC, abstractmethod


class Abstract(ABC):
    def helloworld():
        pass

class hello(Abstract):
    x = "Hello world"
    
    def __init__(self, y):
        self.y = y
    def printing(self):
        print(f"Class variable is: {hello.x}\nInstance variable is: {self.y}")

    @staticmethod
    def helloworld():
        count =1
        print("This is a static method" + "\tCount value is: " + str(count))

obj1 = hello("Sayan")
obj2 = hello("Aryan")

obj1.printing()
obj2.printing()

hello.helloworld()
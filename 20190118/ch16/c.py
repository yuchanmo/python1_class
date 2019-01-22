class Parent:

    def myMethod(self):
        print('Calling parent method')

class Child(Parent):
    def myMethod(self):
        super().myMethod()
        print('Calling child method')

c = Child()
c.myMethod()

isinstance(c,Parent)
issubclass(Child,Parent)


from abc import ABC,abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def func1(self):
        pass
    
    @abstractmethod
    def func2(self):
        pass


b = BaseClass()


from abc import ABC,abstractclassmethod


class AbstractClassExample(ABC):

    def __init__(self,value):
        self.value = value
        super().__init__()

    @abstractclassmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):
    def do_something(self):
        super().do_something()
        return 'Hello'
    

x = DoAdd42(4)
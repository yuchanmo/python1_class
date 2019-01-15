import classintro

v = classintro.Foo()

class BaseClass(object):
    def printHam(self):
        print('ham')


class InheritingClass(BaseClass):
    pass



x = InheritingClass()
x.printHam()
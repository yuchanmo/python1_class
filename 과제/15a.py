#Simple OOP

class Animal:
    
    def __init__(self):
        print('Animal created')
    
    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print('Dog created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('Aoof')

d = Dog()
d.whoAmI()
d.eat()
d.bark()


from math import pi
class Circle:
    p = pi
    def __init__(self):
        self.__radius__ = 0

    def setRadius(self,radius):
        self.__radius__ = radius

    def getRadius(self):
        return self.__radius__
    
    def area(self):        
        #assert type(self.__radius__) == 'int'
        return self.p * (self.__radius__**2)
    
   

c = Circle()
c.setRadius(5)
print(c.getRadius())
print(c.area())
    


class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobdy has claimed to make this shape yet"

    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2*self.x + 2*self.y
    
    def describe(self,text):
        self.description = text

    def authorName(self,text):
        self.author = text

    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale


rectangle = Shape(100,45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe('A wide rectangle,more than twice as wide as it is tall')
rectangle.scaleSize(0.5)

print(rectangle.area())



class Square(Shape):

    def __init__(self, x,y):
        
        super().__init__(x,x)
        super().describe('This is square')

    
class DoubleSquare(Shape):

    def __init__(self, x, y):
        super().__init__(y, y*2)


class InsideDoubleSquare(Square):

    def __init__(self, x, y):
        super().__init__(x, x)
        self.innersquare = Square(x/2,x/2) 
        




s = Square(3,4)
s.perimeter()
s.area()

    
    
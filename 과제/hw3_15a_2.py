#정답
#5
#78.53981633974483

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
    

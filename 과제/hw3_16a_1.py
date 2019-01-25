
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Pythagoras:
    '''Implement the Pythagoras Class'''
    def __init__(self):
        pass

    def setPointOne(self,p1):
        self.point1 = p1
    
    def setPointTwo(self,p2):
        self.point2 = p2

    def getSlope(self):                      
        try:
            return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        except ZeroDivisionError as ze:
            print('x values of both point1 and point2 are same')
        

    def getDistance(self):
        xskewpow = (self.point2.x - self.point1.x)**2
        yskewpow = (self.point2.y - self.point1.y)**2
        return (xskewpow + yskewpow)**0.5

    
# #TestCode
# p1 = Point(0,0)
# p2 = Point(3,4)

# ps = Pythagoras()
# ps.setPointOne(p1)
# ps.setPointTwo(p2)

# ps.getDistance()
# ps.getSlope()



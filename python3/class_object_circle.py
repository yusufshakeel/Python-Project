#circle class
import math

class Circle:
    def __init__(self, r=0):
        self.radius = r

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius


#create object
c1 = Circle()       #this create a circle object of radius = 0 [default value of r]
c2 = Circle(5)      #this create a circle object of radius = 5

#access object field [variable]
print(c1.getRadius())
print(c2.getRadius())
print(c2.getArea())


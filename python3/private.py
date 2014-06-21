#private variable

import math

class Circle:
    def __init__(self, radius = 1):
        self.__radius = radius      #private variable

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi
    
    def getArea(self):
        return math.pi * self.__radius * self.__radius

def main():
    c = Circle(5)
    r = c.getRadius()
    print("Radius:", r)

main()

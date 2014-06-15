#distance between two points
#point A, B
#coord A = x1,y1
#coord B = x2,y2
#using pythagorean theorem

#import sqrt and pow functions from math module
from math import sqrt, pow

#function definition
def dist(x1,y1,x2,y2):
    return sqrt(pow((x1-x2) , 2.0) + pow((y1-y2) , 2.0))

#input
print "Enter ccoord of two points:"
x1,y1 = input("A: x1= "), input("A: y1= ")
x2,y2 = input("A: x2= "), input("A: y2= ")

#output
print "Dist between point A and B = ", dist(x1,y1,x2,y2)

#distance between two points
#point A, B
#coord A = x1,y1
#coord B = x2,y2
#using pythagorean theorem

from math import sqrt, pow

#input
print "Enter ccoord of two points:"
x1,y1 = input("A: x1= "), input("A: y1= ")
x2,y2 = input("A: x2= "), input("A: y2= ")


#compute
dist = sqrt(pow((x1-x2) , 2) + pow((y1-y2) , 2))

#output
print "Dist between point A and B = ", dist

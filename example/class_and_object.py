#class and object

#create a point class
#add to form (variable or attributes)
class Point:
    pass

#create object of class
pobj = Point()

#type
print type(Point)
print type(pobj)

#add new attribute to object pobj
pobj.x = 10
pobj.y = 20

#print value
print "Coord: (%d,%d)" %(pobj.x, pobj.y)

#but this approach of creating class is not good for the purpose.
#we want x and y variable to be the part of class so that each object
#when instantiated have x and y



#initialization method and self helps to address this problem
#it create a class that has an __init__() function to create class having variables
#create a class Point2D contining x and y
class Point2D:
    def __init__(self, x = 0, y = 0):       #default value of x and y will be 0
        self.x = x
        self.y = y

#create object
p2dobj = Point2D(10, 20)

#print type
print type(Point2D)
print type(p2dobj)

#print x and y
print "Coord: (%d,%d)" %(p2dobj.x, p2dobj.y)

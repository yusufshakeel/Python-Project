#class and object

#create a class
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #when defining a method or function, the first parameter refers to the instance being created
    #It is mandatory to name this parameter 'self'
    def distFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    #this function will add n to x and m to y
    def addNM(self, n=0, m=0):
        self.x += n
        self.y += m


#create object
p2dobj = Point2D(3,4)

#print
print "Coord: (%d,%d)" %(p2dobj.x, p2dobj.y)

#print dist from origin
print "Distance from origin: %f" % p2dobj.distFromOrigin()

#add 10 and 20 to x and y
p2dobj.addNM(10,20)

#print new value
print "Coord: (%d,%d)" %(p2dobj.x, p2dobj.y)

#function to find area

#function definition
def circle(r):
    return 3.14159 * r**2

def square(s):
    return s*s

def rectangle(l,b):
    return l*b

def cube(s):
    return 6*s*s


#input
x = input("Enter x: ")
print "Area"
print "Circle: ", circle(x)
print "Square: ", square(x)
print "Rectangle: ", rectangle(x+10, x)
print "Cube: ", cube(x)

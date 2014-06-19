#class and function

#create a time class
class Time:
    pass

#create an object of time
t = Time()

#assign attributes
t.hh = 10
t.mm = 20
t.ss = 30

#add time - pure function
#a function is called pure if it does not change (modify) the content of other variables or functions
#pure function just return values
#it also has no side-effets such as displaying a value or getting user input
def addTime(t1, t2):
    s = Time()      #create object
    s.hh = t1.hh + t2.hh
    s.mm = t1.mm + t2.mm
    s.ss = t1.ss + t2.ss

    if s.ss >= 60:
        s.ss -= 60
        s.mm += 1

    if s.mm >= 60:
        s.mm -= 60
        s.hh += 1
        
    return s


def printTime(t):
    print t.hh, ":", t.mm, ":", t.ss



#create object of time class
#and add new attribute to the objects
tobj1 = Time()
tobj1.hh = 10
tobj1.mm = 20
tobj1.ss = 30

tobj2 = Time()
tobj2.hh = 10
tobj2.mm = 20
tobj2.ss = 30

f = addTime(tobj1, tobj2)       #this will return an object of Time
print "sum: ", printTime(f)

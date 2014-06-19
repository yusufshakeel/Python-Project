#class and methods
#functions that are defined inside the body of the class are called methods

#create a class time
class Time:
    #define method __init__
    #this methods is called when an object of the class is instantiated
    def __init__(self, hh=0,mm=0,ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    #define method that will print the time
    def printTime(self):
        print str(self.hh) + ":" + str(self.mm) + ":" + str(self.ss)


#create object of class Time
tobj = Time(10,20,30)   #set hh=10, mm=20, ss=30
tobj.printTime()

#optional argument
#create object
t2 = Time()         #this will set default values
t2.printTime()


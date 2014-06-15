#speed distance time

#function definition
#Note! converting one of the operand to float in order to avoid integer division
def speed(d,t):
    return float(d)/t

def dist(s,t):
    return float(s)*t

def time(s,d):
    return float(d)/s

#input
s = input("Enter Speed: ")
d = input("Enter Distance: ")
t = input("Enter Time: ")

#output
print "Speed: " + str(speed(d,t))
print "Distance: " + str(dist(s,t))
print "Time: " + str(time(s,d))

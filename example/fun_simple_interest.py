#simple interest example

#function definition
#param p = principal
#param r = rate
#param t = time
def si(p,r,t):
    i = p*(r/100.0)*t   #using 100.0 to get float value
    return i


#input
print "Simple Interest Example"
p = input("Enter Principal P: ")
r = input("Enter Rate R: ")
t = input("Enter Time T: ")

#compute
interest = si(p,r,t)    #function call

#output
print "Interest I: " + str(interest)

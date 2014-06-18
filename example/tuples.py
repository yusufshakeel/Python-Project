#tuple program
#a tuple is a comman separated value

#create a tuple
tup = (1,2,3,4,5,6)
print tup           #print tuple content
print type(tup)     #print type
print len(tup)      #no. of elem in the tuple

#create a single element type
tupSingle = (1,)    #don't forget the ,
print tupSingle
print type(tupSingle)

#accessing elements of a tuple
tup = (1,2,3,4,5,6)
print tup[3]            #this will print the element at index 3
print tup[2:4]          #slice - select element index 2 and index 3

#replace index 3 element with 0
print "before: ", tup
l = list(tup)           #step 1 - convert tuple to list
l[3] = 0                #step 2 - replace (update) value
tup = tuple(l)          #step 3 - convert list to tuple
print "after: ", tup


#swap two variables
a = 1
b = 2
print "before: a = ", a, "\tb = ", b
tmp = a
a = b
b = tmp
print "before: a = ", a, "\tb = ", b

#swap python style
a = 1
b = 2
print "before: a = ", a, "\tb = ", b
a,b = b,a
print "before: a = ", a, "\tb = ", b

#function returning tuple
def swapAB(a,b):
    return b,a

a = 1
b = 2
a,b=swapAB(a,b)
print a,b

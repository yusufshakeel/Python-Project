#program to find max element in the list

#function definition
def recMax(mylist):
    m = mylist[0]                   #set max m to 1st elem of list
    while type(m) == type([]):      #m is a list
        m = m[0]
        
    for elem in mylist:
        if type(elem) == type([]):
            melem = recMax(elem)
            if m < melem:
                m = melem
        else:
            if m < elem:
                m = elem

    return m

l = [[[3,4],5],1,2,6]
print recMax(l)

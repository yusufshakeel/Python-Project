#find sum of all the elements of the list

#function definition
def recSum(mylist):
    s = 0
    for elem in mylist:
        if type(elem) == type([]):      #element of the list is also a list
            s = s + recSum(elem)
        else:
            s += elem
    return s

l = [1,2,3,[4,5,6],[7,8,],9,10]
print recSum(l)

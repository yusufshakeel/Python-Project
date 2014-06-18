#array are list

#1d array
marks = [10,20,30,40,50]

#print all elements
print marks

#print using loop
for x in marks:
    print x

#update element at index 0
marks[0] = 60
print marks

#delete element at index 0
del marks[0]
print marks

#insert new element at index 0
marks.insert(0, 10)
print marks


#2d array
val = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]

#print 2d val
print val

#print using loop
for x in val:       #get list
    for v in x:     #get value in the list
        print v,
    print

#update element at pos 0,0 i.e., 1st row and 1st col
val[0][0] = 10
print val

#delete element at pos 0,0
del val[0][0]
print val

#insert new element at index 0,0
val[0].insert(0,1)      #select 1st row and then use insert to add new element
print val

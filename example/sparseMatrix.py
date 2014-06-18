#sparse matrix
#we use list to create matrix - both 1D and 2D

#create a 4x4 sparse matrix using list
smat = [[0,0,1,0],
        [0,0,0,1],
        [2,0,0,0],
        [0,2,0,0]
        ]

#print sparse matrix
print smat

#print using loop
for l in smat:
    for v in l:
        print v,
    print

#update element at 0,0
smat[0][0] = 1
print smat

#delete element at 0,0
del smat[0][0]
print smat

#insert new element at 0,0
smat[0].insert(0, 0)
print smat



#sparse matrix using dictionary
#key is in tuple (r,c) form
#value is the element
smat = {(0,2): 1,
        (1,3): 1,
        (2,0): 2,
        (3,1): 2
        }

#print smat
print smat

#print using tuple
print smat[(0,2)]

#we can use get() to get the value in spares matrix
#get() function takes two argument separated by comma
#first is key in the form of tuple and second is 0
#if the key is not present in the smat dictionary then 0 is printed
print smat.get((0,0), 0)    #this will print 0 as (0,0) key not in the dictionary
print smat.get((0,2), 0)    #this will print 1



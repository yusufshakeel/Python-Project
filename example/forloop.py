#for loop program

#print the character of the name using for loop
name = 'Yusuf Shakeel'
for ch in name:
    print ch


#for loop a list
#print fruits name and their length
fruits = ['apple', 'banana', 'orange', 'pineapple', 'watermelon']
for f in fruits:
    print f, len(f)


#for loop a list
#print index and fruits name
for f in range(len(fruits)):
    print f, fruits[f]


#print from 1 to 10
#range syntax - range[x,y]
#where x in included and y is excluded. so range starts from x and go up to y-1
for i in range(1,11):
    print i


#print from 5 to 9
for i in range(5,10):
    print i


#print the AP series of 5 i.e., 5, 10, 15, 20, till 30
#range syntax - range[x,y,step]
#where x is start index (included)
#y is end index (excluded)
#step is the increment
for i in range(5,31,5):
    print i,


#print the series -10, 20, 50, 80, till 200
for i in range(-10,201,30):
    print i,

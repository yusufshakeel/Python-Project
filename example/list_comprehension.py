#list comprehension
#to create list from other list using some mathematical syntax
#syntax:
#[expr for item1 in seq1 for item2 in seq2 ... for itemN in seqN if condition]


#list
num = [1,2,3,4]
print num

#create list having element value square of num
print [x**2 for x in num]

#create list having element value double of num
print [x*2 for x in num]

#create list having element value square of num and greater than 6
print [x**2 for x in num if x**2 > 8]

#create a list containing tuple
print [(x,x**2,x**3) for x in num]

#create a list of extension
keyword = ['file', 'bin', 'lib', '.exe', '.sh', '.c']
print [x for x in keyword if x[0] == '.']

#create a list of non extension
print [x for x in keyword if x[0] != '.']

#permute letters
letters = ['a','b','c']
print [x*l for x in num for l in letters]

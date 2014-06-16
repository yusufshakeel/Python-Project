#list program

#import functions from modules
import string

#print list content using while loop
fruits = ['apple', 'orange', 'mango', 'banana']
i = 0
s = len(fruits)
while i < s:
    print fruits[i]
    i+=1

#print list content using for loop
for i in range(0,s):
    print fruits[i]


#list concatenate
list1 = [1,2,3]
list2 = [2,3,4]
list3 = list1+list2
print list3, "List length: ", len(list3)

#list repeat - print list fruits THRICE
print fruits*3

#list slice
print fruits[0:3]       #print 0th,1st,2nd element of the list
print fruits[1:3]       #print 1st and 2nd element of the list
print fruits[:]         #print all elements

#create list of numbers
print range(10)         #list from 0 to 9
print range(2,10)       #list from 2 to 9
print range(1,10,2)     #list of odd numbers from 1 to 9
print range(2,10,2)     #list of even numbers from 2 to 8
print range(9,0,-2)     #list of odd numbers from 9 to 1
print range(10,0,-2)    #list of even numbers from 10 to 2
print range(10,20,-2)   #empty list - note! when step size is -ve then start must be greater than stop

#list are mutable
#list of os
os = ['win', 'osx', 'fedora', 'ubuntu']
print os

#update element
os[0]='windows'         #0th element modified
print os

#delete element using slices
os[0:1]=[]              #0th element removed
print os

#add element
os[0:0]=['windows']     #0th element added
print os

#delete element using del
del os[0]               #delete 0th element
print os

#add element
os[0:0]=['windows']     #add 0th element
print os

#delete element using del and slices
del os[0:1]             #delete 0th element
print os

#add element
os[0:0]=['windows']     #add 0th element
print os


#clone a list - make a copy of a given list
newOSlist = os[:]       #this will copy the content of the os list in newOSlist
print newOSlist


#enumerate - generates index and value associated with the list
for index, value in enumerate(newOSlist):
    print index,value


#multiple all element of the list by 2
#function to multiply 2
#reference of the original list is passed to this function
#so, any change made to mylist here in this function is reflected back to the original list
def multiply2(mylist):
    for index,value in enumerate(mylist):
        mylist[index] = value*2

#number list
number=[1,2,3,4,5]
print number            #before function call
multiply2(number)       #function call
print number            #after function call


#create a list from a string - joining the element of the list to form a string
l = list("hello")       #this creates a list
print l                 #this will print ['h','e','l','l','o']
m = string.join(l,'')   #this will join the element of the list l
print m                 #this will print hello


#split string - this will create a list by splitting the string
s = 'my name is yusuf shakeel'  #this is a string
print s, "[Len:", len(s), "]"   #this will print s and length of s
l = string.split(s)             #this will split the string s into a list
print l, "[Elem:", len(l), "]"  #this will print element of list l and no. of element in it


#split string using delimiter - this will split the string s using the delimiter d
s = 'monday tuesday wednesday thrusday friday saturday sunday'
print s
l = string.split(s, 'day')      #this will split s from the dilimiter 'day'
print l


#list functions
mylist = [1,2,3]                #create a list
print mylist

mylist.append(4)                #append 4 to mylist
print mylist

mylist.insert(1,2)              #insert 2 at index 1
print mylist

n = mylist.count(2)             #count no. of 2 in the list
print n

mylist.extend([5,8,6,7,9])      #add a new list at the end of mylist    
print mylist

print mylist.index(2)           #return first index of element

mylist.reverse()                #this will reverse the element of mylist
print mylist

mylist.sort()                   #this will sort the list
print mylist

mylist.remove(2)                #this will remove the first occurance of the element
print mylist

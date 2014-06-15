#prime number from 2 to N

#import function from modules
from math import sqrt

#input
n = input("Enter n: ")

#compute
for i in range(2, n+1):
    flag = 0
    for x in range(1, i+1):
        if i%x==0:
            flag+=1
        if flag > 2:
            break
    if flag==2:
        print i, "is prime"

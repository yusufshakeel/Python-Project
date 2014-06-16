#list of keywords

#import function from modules
from keyword import *

#print all keywords
print kwlist

#iskeyword
k = raw_input("Enter a word: ")
if iskeyword(k):
    print "'%s' is a keyword." %k
else:
    print "%s is not a keyword." %k


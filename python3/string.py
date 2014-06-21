#all about string

#create string
s1 = ""         #empty string
s2 = "hello"    #string hello

#create string using str
s1 = str()          #same as ""
s2 = str("hello")   #same as "hello"

'''
note
string are immutable
two or more string object having the same value are shares the same object
'''

#assign value to s1 string object
s1 = "hello"

#length of the string
print(len(s1))

#largest character in string
print(max(s1))

#smallest character in string
print(min(s1))


#string
s = "python"

#index operator
print(s[0])     #0th element i.e., p
print(s[-1])    #last element i.e., n

#print characters at even index
for i in range(0, len(s), 2):
    print(s[i], end="")

#slice
print(s[0:2])   #print element at index 0,1
print(s[2:])    #print element from index 2 to last
print(s[:])     #print all
print(s[2:-1])  #print element from index 2 to second last

#concatenate +
print("hello " + s)

#repeat
print(s*3)  #print 'python' thrice

#test for string
print("come" in "welcome")  #is 'come' in the word 'welcome'
print('hello' not in 'python')

#compare
print("hello" == "hello")
print("green" != "blue")
print("a" < "b")
print("c" > "C")    #comparing ASCII value
print("abc" >= "ABC")
print("XYZ" <= "xyz")

#print string s character by character
for ch in s:
    print(ch)

#testing string
print("hello".isalnum())    #True
print("132".isalnum())      #True
print("<?>".isalnum())      #False
print("abc".isalpha())      #True
print("123".isdigit())      #True
print(s.isidentifier())     #True
print("abc".islower())      #True
print("ABC".isupper())      #True
print(" ".isspace())        #True

#substring search
#s = "python"
print(s.endswith("thon"))   #True
print(s.startswith("py"))   #True
print(s.find("th"))         #smallest index where 'th' occurs
print(s.rfind("th"))        #largest index where 'th' occurs
print(s.count('th'))        #count number of substring

#covert string
#s = "python"
#as string is immutable so the following functions will return a copy of the modified string
print(s.capitalize())       #first letter capitalize
print(s.lower())            #convert to lower case
print(s.upper())            #convert to upper case
print(s.swapcase())         #swapcase
print(s.replace('p','j'))   #replace all occurance of 'p' with 'j'

#remove white spaces = ' ', '\t', '\f', '\r' and '\n'
print("   hello".lstrip())  #remove leading white space
print("hello   ".rstrip())  #remove trailing white space
print("  hello ".strip())   #remove leading and trailing white space

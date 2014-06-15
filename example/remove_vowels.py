#program to remove vowels from string

#function definition
def removeVowels(s):
    v = 'aeiouAEIOU'
    tmp = ''
    for ch in s:
        if ch not in v:
            tmp += ch
    return tmp

#input
x = raw_input("Enter string: ")
print "String without vowels: ", removeVowels(x)

#program to count fequency of letters

letterFreq = {}     #empty dictionary

s = raw_input("Enter string: ")

for letter in s:
    letterFreq[letter] = letterFreq.get(letter,0)+1

freqList = letterFreq.items()
freqList.sort()
print freqList

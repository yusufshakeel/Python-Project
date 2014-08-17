'''
SAMPLE INPUT
Hello World
PESSE ACM
Good Day

OUTPUT
World Hello
ACM PESSE
Day Good
'''



import sys
for line in sys.stdin:
	line=line.strip("\n")
	s=list(line.split(' '))
	s.reverse()
	for x in s:
		print x,
	print
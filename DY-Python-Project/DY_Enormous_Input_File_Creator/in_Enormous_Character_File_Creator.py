'''
Author: Yusuf Shakeel
Date: 09-July-2014 Wednesday
Version: 1.0.0710

Requirement:
-------------
To run this code you need Python installed on your computer.

How to generate input file?
----------------------------
1.  Copy this file to a folder [directory] where you want to create the
    input file.

2.  Enter an integer value from 1 to 1000000000 (both inclusive) to generate
    the input file.
'''

from random import randint

print("\
DY Enormous Character File Creator\n\
Author: Yusuf Shakeel\n\
Date: 09-July-2014 Wednesday\t\
Version: 1.0.0710\n\n\
The MIT License\nCopyright (c) 2014 Yusuf Shakeel\n\n\
https://github.com/yusufshakeel\n\
https://www.facebook.com/yusufshakeel\n\
https://www.youtube.com/yusufshakeel\n\
https://plus.google.com/+YusufShakeel\n\
https://www.twitter.com/yusufshakeel\n\
--------------------------------------------------\n\
Note!\n\
This program will create enormous input file consisting of\n\
ASCII characters [34-126 ASCII value]\n\
You will be prompted to enter an integer value from 1 to 1000000000.\n\n\
Integer Value\tFile Size (approx)\n\
-------------\t------------------\n\
10           \t10     bytes\n\
100          \t100    bytes\n\
1000         \t1000   bytes\n\
10000        \t9.76   KB\n\
100000       \t97.6   KB\n\
1000000      \t976    KB\n\
10000000     \t9.54   MB\n\
100000000    \t95.37  MB\n\
1000000000   \t953.67 MB\n\
10000000000  \t9.31   GB\n\n\
Output File name: in<YOUR_INTEGER_VALUE>char.dat\n\
Example: If you entered say 1000 then output file will be in1000char.dat\n\
\nWARNING!!!\n\
File size is directly proportional to the integer value you enter.\n\
If your integer value is very large (say more than 1000000000) then\n\
the input file created will be huge. THE FILE SIZE MAY GO OVER 1 GB!\n\
So be careful while entering your integer value.\
\n\n\n")

no_of_bytes = input("Enter an integer value [Safe Range: 1 to 1000000]: ")
if no_of_bytes > 0:
	fname = "in"+str(no_of_bytes)+"char.dat"
	myfile = open(fname,'w')
	for i in range(no_of_bytes):
		myfile.write(str(chr(randint(34,126))))
	myfile.close()
print("END OF PROGRAM\n")
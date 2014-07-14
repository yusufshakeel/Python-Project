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
DY Enormous Input Test File Creator\n\
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
This program is used to create enormous input file.\n\
You will be prompted to enter an integer value from 1 to 1000000000.\n\n\
Integer Value\tFile Size in MB (approx)\n\
-------------\t------------------------\n\
100000       \t1.03 MB\n\
200000       \t2.07 MB\n\
250000       \t2.59 MB\n\n\
Output File name: en<YOUR_INTEGER_VALUE>int.dat\n\
Example: If you entered say 1000 then output file will be en1000int.dat\n\
\nWARNING!!!\n\
File size is directly proportional to the integer value you enter.\n\
If your integer value is very large (say more than 1000000000) then\n\
the input file created will be huge. THE FILE SIZE MAY GO OVER 1 GB!\n\
So be careful while entering your integer value.\
\n\n\n")

no_of_lines = input("Enter an integer value [Safe Range: 1 to 1000000]: ")
if no_of_lines > 0:
	fname = "en"+str(no_of_lines)+"int.dat"
	myfile = open(fname,'w')
	myfile.write(str(no_of_lines)+" 3\n")
	for i in range(no_of_lines):
		myfile.write(str(randint(0,1000000000)))
		if i < no_of_lines - 1:
			myfile.write("\n")
	myfile.close()
print("END OF PROGRAM\n")
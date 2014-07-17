'''
Author: Yusuf Shakeel
Date: 14-July-2014 Monday
Version: 1.0.0714

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

print("\
DY Enormous Number File Creator\n\
Author: Yusuf Shakeel\n\
Date: 14-July-2014 Monday\t\
Version: 1.0.0714\n\n\
The MIT License\nCopyright (c) 2014 Yusuf Shakeel\n\n\
https://github.com/yusufshakeel\n\
https://www.facebook.com/yusufshakeel\n\
https://www.youtube.com/yusufshakeel\n\
https://plus.google.com/+YusufShakeel\n\
https://www.twitter.com/yusufshakeel\n\
--------------------------------------------------\n\
Note!\n\
This program will create enormous input file consisting of digits [0-9].\n\
You will be prompted to enter an integer value from 1 to 1000000000.\n\n\
Output File name: in<YOUR_INTEGER_VALUE>num.dat\n\
Example: If you entered say 1000 then output file will be in1000num.dat\n\
\nWARNING!!!\n\
File size is directly proportional to the integer value you enter.\n\
If your integer value is very large (say more than 1000000000) then\n\
the input file created will be huge. THE FILE SIZE MAY GO OVER 1 GB!\n\
So be careful while entering your integer value.\
\n\n\n")

no = input("Enter an integer value [Safe Range: 1 to 1000000]: ")
if no > 0:
	fname = "in"+str(no)+"num.dat"
	myfile = open(fname,'w')
	myfile.write(str(no)+"\n")
	for i in range(1,no):
		myfile.write(str(i)+"\n")
	myfile.write(str(no))
	myfile.close()
print("END OF PROGRAM\n")
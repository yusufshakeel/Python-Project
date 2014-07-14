'''
Author: Yusuf Shakeel
Date: 09-July-2014 Wednesday
Version: 1.0.0710
'''

from random import randint

print("\
DY Password Generator\n\
Author: Yusuf Shakeel\n\
Date: 10-July-2014 Thursday\t\
Version: 1.0.0710\n\n\
The MIT License\nCopyright (c) 2014 Yusuf Shakeel\n\n\
https://github.com/yusufshakeel\n\
https://www.facebook.com/yusufshakeel\n\
https://www.youtube.com/yusufshakeel\n\
https://plus.google.com/+YusufShakeel\n\
https://www.twitter.com/yusufshakeel\n\
--------------------------------------------------\n\n\
Note!\n\
You will be asked to enter the number of character you want in your password.\n\
Choose a number from 6 to 1024.\n\
Your password can have maximum 1024 characters.\n\
THOUGH 32 CHARACTERS ARE VERY STRONG!\n\n\
Output File: dy_password.txt\
\n")

no_of_char = input("Enter the number of characters you want in your password: ")

if no_of_char > 5 and no_of_char < 1025:
	fname = "dy_password.txt"
	myfile = open(fname,'w')
	myfile.write("Your Password:\n\n")
	for i in range(no_of_char):
		x = randint(1,4)
		if x == 1:
			myfile.write(str(chr(randint(48,57))))		#0-9
		elif x == 2:
			myfile.write(str(chr(randint(65,90))))		#A-Z
		elif x == 3:
			myfile.write(str(chr(randint(97,112))))		#a-z
		elif x == 4:
			x = randint(1,15)
			if x == 1:
				myfile.write("!")		#symbol
			elif x == 2:
				myfile.write("@")		#symbol
			elif x == 3:
				myfile.write("#")		#symbol
			elif x == 4:
				myfile.write("$")		#symbol
			elif x == 5:
				myfile.write("%")		#symbol
			elif x == 6:
				myfile.write("^")		#symbol
			elif x == 7:
				myfile.write("&")		#symbol
			elif x == 8:
				myfile.write("*")		#symbol
			elif x == 9:
				myfile.write("(")		#symbol
			elif x == 10:
				myfile.write(")")		#symbol
			elif x == 11:
				myfile.write("{")		#symbol
			elif x == 12:
				myfile.write("}")		#symbol
			elif x == 13:
				myfile.write("[")		#symbol
			elif x == 14:
				myfile.write("]")		#symbol
			elif x == 15:
				myfile.write("|")		#symbol
	myfile.write("\n\nNumber of characters: "+str(no_of_char))		
	myfile.write("\n\n\n\
DY Password Generator\n\
Author: Yusuf Shakeel\n\
Date: 10-July-2014 Thursday\t\
Version: 1.0.0710\n\n\
The MIT License\nCopyright (c) 2014 Yusuf Shakeel\n\n\
https://github.com/yusufshakeel\n\
https://www.facebook.com/yusufshakeel\n\
https://www.youtube.com/yusufshakeel\n\
https://plus.google.com/+YusufShakeel\n\
https://www.twitter.com/yusufshakeel\n\
")
	myfile.close()
elif no_of_char > 1024:
	print("\nPlease choose a number from 6 to 1024.\n")
print("END OF PROGRAM\n")
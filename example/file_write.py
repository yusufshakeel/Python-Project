#this program will create a file and write some text in it.

#open a file.
#if file by that name is present then it is overwritten
#if no file by that name exists in the directory then a new file is created
#open() function creates a file object
myfile = open('myfile.txt','w')

#print file detail
print myfile

#write text
myfile.write("Hello World!")

#close file object
myfile.close()

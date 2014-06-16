#this program is about file reading

#open file
#to open a file we use the 'r' mode
myfile = open('myfile.txt','r')

#read all the content at once
#to read the file content we use the read() function
#read() returns a string which we can store in a variable (i.e., attribute)
s = myfile.read()
print s

#close file
myfile.close()

#open file
myfile = open('myfile.txt','r')

#to read N number of characters
s = myfile.read(5)          #this will read only 5 characters
print s

#close file
myfile.close()

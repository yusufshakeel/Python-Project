#file functions

#create a file and write 3 lines
myfile = open('mytext.txt','w')
myfile.write("hello world!\nhave a nice day.\nhave fun!")
myfile.close()

#open same file - read mode
myfile = open('mytext.txt','r')
print myfile.readline(),        #read 1st line
print myfile.readline(),        #read 2nd line
print myfile.readline(),        #read 3rd line
print myfile.readline()         #this will return empty string as we have reached the end of file
myfile.close()

#open same file - read mode
myfile = open('mytext.txt','r')
mytextlist = myfile.readlines()     #this will return all the lines as list of strings
print mytextlist

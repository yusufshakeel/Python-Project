#program to copy content of one file into another file

#function definition
def copyFile(srcFile, destFile):
    src = open(srcFile, 'r')        #read source file
    dest = open(destFile, 'w')      #write destination file
    while True:
        txt = src.read(50)          #read 50 characters at a time
        if txt == "":               #reached end of file
            break
        dest.write(txt)             #write 50 characters stored in txt to destination file
    src.close()                     #close source file
    dest.close()                    #close destination file


#input
src = raw_input("Enter source file path: ")
dest = raw_input("Enter destination file path: ")
copyFile(src, dest)

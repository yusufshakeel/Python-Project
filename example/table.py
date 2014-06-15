#table

#function definition
def table(n):
    i = 1
    while i <= n:
        printMultiple(i)
        i = i + 1

def printMultiple(n):
    i = 1
    while i <= 10:
        print i*n, "\t",
        i = i + 1
    print

x = input("Enter x: ")
table(x)

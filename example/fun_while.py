#while loop

#function definition
def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print "Blastoff"

x = input("Enter n: ")
countdown(x)

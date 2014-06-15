#program to print multiple of N

#function definition
def multiple(n):
    i = 1
    while i <= 5:
        print i*n, "  ",
        i = i + 1
    print

x = input("Enter x: ")
print "Multiple :", multiple(x)

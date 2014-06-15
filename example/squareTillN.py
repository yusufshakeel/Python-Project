#program to print square of numbers till N

#function definition
def square(n):
    i = 1
    while i <= n:
        print i, "\t", i**2
        i += 1

x = input("Enter x: ")
square(x)

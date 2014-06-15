#count digit

#function definition
def countDigit(n):
    count = 0
    while n:
        count = count + 1
        n = n / 10
    return count

x = input("Enter x: ")
print "Number of digits: ", countDigit(x)

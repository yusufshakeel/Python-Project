#logical condition - and or not

x = input("Enter x: ")

#and
if x > 0 and x < 10:
    print x, "is in the range 1 to 9"

#or
if x > 0 or x < 10:
    print x, "is greater than 0 or less than 10"

#not
if not(x>10):
    print x, "is less than 10"
else:
    print x, "is greater than 10"


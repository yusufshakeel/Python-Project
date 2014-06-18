#exception handling

#division by zero exception
try:
    a = 1/0
    print a
except:
    print 'Error: Division by zero'


#raise exception
age = input("Enter age: ")
if age < 0:
    raise ValueError, '%s is not a valid age.' %age


#error - max recursion depth reached
def infinitRec(n):
    try:
        infinitRec(n+1)
    except:
        print 'Error: Maximum recursion depth reached.', n

infinitRec(0)


#passing function as parameter

#function definition
def f(x):
    return x+10

def g(x):
    return x+20

def h(x):
    return x+30

def funCall(x,fun):
    return fun(x)

#input
x = input("Enter x: ")

#output
print "+10: ", funCall(x,f)
print "+20: ", funCall(x,g)
print "+30: ", funCall(x,h)

#operator overloading

#its about changing the definition of the built-in operator

#class P overloads + operator
class P:
    #method definition
    #initialization method
    def __init__(self, x=0):
        self.x = x

    #operator overloading: +
    #this method will return values in the form x:y
    def __add__(self,other):
        return str(self.x) + ":" + str(other.x)

#instantiate object
obj1 = P(10)
obj2 = P(20)
r = obj1 + obj2
print r

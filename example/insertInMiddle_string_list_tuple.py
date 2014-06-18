#program to insert a value in the middle of a string, list and tuple

#insert 'c' in the middle of s, l, t

s = 'abde'              #string s
l = ['a','b','d','e']   #list l
t = ('a','b','d','e')   #tuple t

#function definition
#for string
def insert_in_str(val, mystr):
    mid = len(mystr)/2
    return mystr[:mid]+str(val)+mystr[mid:]

#for list
def insert_in_list(val, mylist):
    mid = len(mylist)/2
    mylist[mid:mid] = val

#for tuple
def insert_in_tuple(val, mytup):
    mid = len(mytup)/2
    return mytup[:mid]+(val,)+mytup[mid:]

#insert in string
s = insert_in_str('c', s)
print s

#insert in list
insert_in_list('c', l)
print l

#insert in tuple
t = insert_in_tuple('c', t)
print t


#insert function for all type of sequence - string, list, tuple
def insert_in_middle(val, seq):
    mid = len(seq)/2
    return seq[:mid] + encap(val,seq) + seq[mid:]

def encap(val, seq):
    if type(seq) == type(""):   #string type
        return str(val)
    if type(seq) == type([]):   #list type
        return [val]
    return (val,)               #tuple type

#initial
s = 'abde'              #string s
l = ['a','b','d','e']   #list l
t = ('a','b','d','e')   #tuple t

#insert
s = insert_in_middle('c',s)
print s

l = insert_in_middle('c',l)
print l

t = insert_in_middle('c',t)
print t

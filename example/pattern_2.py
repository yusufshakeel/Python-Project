#pattern programming
#4321
# 321
#  21
#   1
#where n is the no. of lines

#input
n = input("Enter n: ")

#output
for r in range(n,0,-1):         #row
    sp = n;
    while sp > r:               #space
        print " ",
        sp-=1
    for c in range(r,0,-1):     #column
        print c,
    print

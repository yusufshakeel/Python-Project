#pattern printing
# 1
# 12
# 123
# 1234
#where n is the no. of lines

#input
n = input("Enter n: ")

#loop
for r in range(1,n+1):
    for c in range(1,r+1):
        print c,
    print

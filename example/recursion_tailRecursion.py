#tail recursion

def rec(n):
    if n == 0:
        print 'Blastoff!'
    else:
        print n
        rec(n-1)

rec(3)

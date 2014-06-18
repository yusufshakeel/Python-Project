#max recursion depth

def infinitRec(n):
    try:
        infinitRec(n+1)
    except:
        print 'Max Recursion Depth reached: ', n

infinitRec(0)

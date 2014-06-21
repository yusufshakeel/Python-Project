#approx value of pi

n = 10000
s = 1
for i in range(1,n):
    s += ((-1)**i)*(1/((2*i)+1))

pi = 4.0 * s
print('Approx value of PI: ', pi)

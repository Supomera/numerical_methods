# Gauss Seidel Iteration
# Author: @Omer Bera Dinc

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x_1,x_2,x_3,x_4: (4 - 7 * x_2 - 2 * x_3 + 8 * x_4) / 12
f2 = lambda x_1,x_2,x_3,x_4: (2 + 9 * x_1 - 6 * x_3 - 2 * x_4) / 14
f3 = lambda x_1,x_2,x_3,x_4: (-7 - 4 * x_1 - 8 * x_2 - 10 * x_4) / -11
f4 = lambda x_1,x_2,x_3,x_4: (12 - x_1 - 4 * x_2 + 5 * x_3) / -9

# Initial setup (zero vector)
x_1 = 0
x_2 = 0
x_3 = 0
x_4 = 0
count = 1

# Defining tolerable error
e = 10**-3

# Implementation of Gauss Seidel Iteration
print('\nCount\tx_1\tx_2\tx_3\tx_4\n')

condition = True

while condition:
    x1 = f1(x_1, x_2, x_3, x_4)
    y1 = f2(x1,x_2, x_3, x_4)
    z1 = f3(x1,y1, x_3, x_4)
    t1 = f4(x1,y1,z1,x_4)
    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1,t1))
    e1 = abs(x_1-x1);
    e2 = abs(x_2-y1);
    e3 = abs(x_3-z1);
    e4 = abs(x_4-t1);
    
    count += 1
    x_1 = x1
    x_2 = y1
    x_3 = z1
    x_4 = t1
    
    condition = e1>e and e2>e and e3>e and e4>e

print('\nSolution: x=%0.3f, y=%0.3f, z = %0.3f, and t = %0.3f\n'% (x1,y1,z1,t1))
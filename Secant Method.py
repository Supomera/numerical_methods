# Root Finding Algorithms in Numerical Methods, Secant Method
# Author: Ömer Bera Dinç 
# 

import math
# Defining my equation
f = lambda x: -x**6 + 3*x + 7

# defining my function that gets 3 inputs, initial points x0 and x1, and error tolerance
def secant(x0,x1,e):

    #defining "step" to print iteration
    step = 0
    #defining a boolean for a flag
    condition = True
    
    #defining an array that stores my xn to print out xn-1, xn, xn+1. 
    aaarray = [-1, 0]
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        aaarray.append(x2)
        
        x0 = x1
        x1 = x2
        
        print("------------")
        print('n: ',  step, 'xn-1: ', aaarray[step], 'xn: ', aaarray[step + 1], 'xn+1: ', aaarray[step + 2], '|xn+1 - xn|: ', abs(aaarray[step + 2] - aaarray[step + 1]))
        
        step = step + 1
        
        #if this is true, while loop continues
        condition = abs(f(x2)) > e
    print('\n Required root is: ', x2)


# Calling the function
secant(0, 1, 10**-7)


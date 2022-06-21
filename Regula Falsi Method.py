# Root Finding Algorithms in Numerical Methods, Regula Falsi Method
#Author: Ömer Bera Dinç 

#Defining my equation
f = lambda x: x**4 + 7*(x**3) - 11*(x**2) + 5

#Defining my function that takes 3 values which are xlower xupper and error tolerance
def falsePosition(x0,x1,e):
    #Defining step to take iteration info
    step = 1

    #Defining condition value to identify a flag
    condition = True

    #To print absolute of nth xroot - (n-1)th xroot in each iteration (line 22 and line 26) I need to store all xroots, so I defined an array for this.
    aarray = [x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )]
    while condition:
        
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        #appending xroots to my array that I defined before
        aarray.append(x2)
        if f(x0) * f(x2) < 0:
            x1 = x2
            print("--------")
            print('n: ',  step, 'xl: ', x0, 'xu: ', x1, 'xr: ', x2, '|xr^n - xr^(n-1)|: ', abs(aarray[step]) - aarray[step - 1])
        else:
            x0 = x2
            print("--------")
            print('n: ',  step, 'xl: ', x0, 'xu: ', x1, 'xr: ', x2, '|xr^n - xr^(n-1)|: ',  abs(aarray[step]) - aarray[step - 1])

        #continues being true unless f(x2) is not smaller than error tolerance
        condition = abs(f(x2)) > e
        step = step + 1
    print('\nRequired root is: ', x2)


x0 = -2
x1 = 0
# Checking correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    # Calling the function
    falsePosition(x0, x1, 10**-6)
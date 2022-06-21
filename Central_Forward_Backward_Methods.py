# Numerical Methods to find derivative of a function
# Author: @Omer Bera Dinc

import numpy as np
import matplotlib.pyplot as plt

''' Defining my variables here '''

x = np.linspace(2,3,20)
xinitial = 2
xfinal = 3
f = lambda x: (x**3 - 6*x - 3)
y = f(x)
g = lambda x: (3*x**2 - 6)
k = g(x)

def calculating(f,a,method='central'):
    '''
    f : function
    
    a : Calculating derivative of the function at x = a
    
    method : Selecting the method (forward, central, backward) as giving string
    
    h : Step size 

        Difference formulas are:
            central: f(a+h) - f(a-h))/2h
            forward: f(a+h) - f(a))/h
            backward: f(a) - f(a-h))/h
    '''
    
    h = (xfinal - xinitial)/20
    
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method name may be misspelled.")

def tohelpcalculationoferror(g, b):
    return g(b)

''' Defining calculated values '''
dydx = calculating(f,x) #central method results
dydx1 = calculating(f, xinitial, method = 'forward')  #forward method result for the first x
dydx2 = calculating(f, xfinal, method = 'backward') #backward method result for the last x
dYdx = (3*(x**2)) - 6 #real values

''' Finding relative error '''
absoluterror = abs(tohelpcalculationoferror(g, x) - dydx)
relativerror = ( absoluterror / dydx ) * 100

''' Printing relative error as array '''
print(relativerror)

''' Firstly plotting real values, then calculated ones'''
plt.figure(figsize=(12,5))
plt.plot(x,dYdx, 'b', label='True Value')

''' Plots relative error to the graph '''
#plt.plot(x, relativerror, 'r.', label = 'Relative Error')

plt.plot(x,dydx, 'r.', label="Central Difference")
plt.plot(xinitial, dydx1, 'g.', label = 'Forward Difference')
plt.plot(xfinal, dydx2, 'k.', label = 'Backward Difference')
plt.legend()
plt.grid(True)

plt.show()

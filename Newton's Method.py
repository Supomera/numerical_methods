# Root Finding Algorithms in Numerical Methods, Newton's Method
#Author: Ömer Bera Dinç

import numpy as np
import math

# Since I did not write the iteration with loops, I defined the number of iterations with self and then increased it as I called the function. So I needed class structure.
class numericalmethods:
    
    def __init__(self):
        #self.n = Iteration variable
        self.n = 0
        # defining my equation here 
        self.f = lambda x: x**(1/3) + np.log(x)

        # defining the derivative of my equation here
        self.f_prime = lambda x: 1/(3*(x**(2/3))) + 1/x

        # calling my function, it takes 4 variables, equation (self.f), derivative of equation (self.f_prime), initial point
        estimate = self.my_newton(self.f, self.f_prime, 1, 10**-7)
        print("estimated root =", estimate)
    
    def my_newton(self, f, df, x0, tol):
        # output is an estimation of the root of f 
        # using the Newton Raphson method
        # recursive implementation
        self.n += 1
        print("--------------")
        
        if abs(self.f(x0) / self.f_prime(x0)) < tol:
            print("n: ", self.n, "xn: ", x0, "f(xn): ", self.f(x0), "f'(xn): ", self.f_prime(x0), " xn+1: ", x0 - f(x0)/df(x0), "|xn - xn+1| ", abs(f(x0)/df(x0)) )
            return x0
        else:
            print("n: ", self.n, "xn: ", x0, "f(xn): ", self.f(x0), "f'(xn): ", self.f_prime(x0), " xn+1: ", x0 - f(x0)/df(x0), "|xn - xn+1| ", abs(f(x0)/df(x0)) )
            return self.my_newton(f, df, x0 - f(x0)/df(x0), tol)
    
if __name__ == "__main__":
    numericalmethods()
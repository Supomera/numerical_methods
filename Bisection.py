# Root Finding Algorithms in Numerical Methods, Bisection Method
#Author: Ömer Bera Dinç
import numpy as np

# Since I did not write the iteration with loops, I defined the number of iterations with self and then increased it as I called the function. So I needed class structure.
class numericalmethods:
        
    def __init__(self):
        #self.n = Iteration variable
        self.n = 0

        #defining my equation
        self.f = lambda x: x**4 + 7*(x**3) - 11*(x**2) + 5
        
        #calling my function, variables it takes are function (self.f), xlower, xupper, error tolerance
        self.xr = self.bisectionalgo(self.f, -2, 0, 10**-5)

        #printing found xroot and f(xroot)
        print("xr =", self.xr)
        print("f(xr) =", self.f(self.xr))

       
    def bisectionalgo(self, f, xlow, xup, tol): 
        
        print("---------------------------------")
        self.n += 1
        # approximates xlow root, R, of f bounded by xlow and xup to within tolerance | f(xes) | < tol with xes the midpoint between xlow and xup Recursive implementation
        
        # check if xlow and xup bound a root
        if np.sign(f(xlow)) == np.sign(f(xup)):
            raise Exception(
             "The scalars xlow and xup do not bound a root")
            
        # get midpoint
        xes = (xlow + xup)/2
        
        if np.abs(f(xes)) < tol:
            # stopping condition, report xes as root
            print("n: ", self.n, "xl: ", xlow, "xu: ", xup, "xr: ", xes, " |xu - xr|: ", abs(xup - xes), "f(xr): ", f(xes) )
            return xes
        elif np.sign(f(xlow)) == np.sign(f(xes)):
            # case where xes is an improvement on xlow. Make recursive call with xlow = xes
            print("n: ", self.n, "xl: ", xlow, "xu: ", xup, "xr: ", xes, " |xu - xr|: ", abs(xup - xes), "f(xr): ", f(xes) )
            return self.bisectionalgo(f, xes, xup, tol)
        elif np.sign(f(xup)) == np.sign(f(xes)):
            # case where xes is an improvement on xup. Make recursive call with xup = xes
            print("n: ", self.n, "xl: ", xlow, "xu: ", xup, "xr: ", xes, " |xu - xr|: ", abs(xup - xes), "f(xr): ", f(xes) )
            return self.bisectionalgo(f, xlow, xes, tol)
        
if __name__ == "__main__":
    numericalmethods()
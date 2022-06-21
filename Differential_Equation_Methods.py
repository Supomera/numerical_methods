# Numerical Methods for Differential Equations
# @Author: Omer Bera Dinc

import math
import matplotlib.pyplot as plt
import numpy as np


class DiffEquationMethods:

    def __init__(self):
        
        #This is only for getting real values one by one 
        x = [0,1,2,3,4,5] 
        fresult = []
        a = 0
        while a < 6:
        
            f = x[a]**3 + 3*x[a]**2 + 6*x[a] - 3*math.exp(x[a]) + 6
        
            fresult.append(f)
            a += 1

        #Defining my variables
        self.i = 0
        self.yi = [3]
        self.h = 1
        self.xi = [0]
        
        #Iterating Euler Method 
        while self.i < 5: 
            self.euler_method()
            self.i += 1
            
        #THESE ARE TRUE VALUES
        plt.figure(figsize=(12,5))
        plt.plot(x[0], fresult[0], 'b.', label = 'True Value')
        plt.plot(x[1], fresult[1], 'b.')
        plt.plot(x[2], fresult[2], 'b.')
        plt.plot(x[3], fresult[3], 'b.')
        plt.plot(x[4], fresult[4], 'b.')
        plt.plot(x[5], fresult[5], 'b.')
        
        #THESE ARE EULER VALUES
        plt.plot(self.xi[0], self.yi[0], 'r.', label = 'Euler Value')
        plt.plot(self.xi[1], self.yi[1], 'r.')
        plt.plot(self.xi[2], self.yi[2], 'r.')
        plt.plot(self.xi[3], self.yi[3], 'r.')
        plt.plot(self.xi[4], self.yi[4], 'r.')
        plt.plot(self.xi[5], self.yi[5], 'r.')
        
        #Wrote reset function to go back to the initial values
        self.reset()
        
        #Iterating midpoint method 
        while self.i < 5: 
            self.midpoint_method()
            self.i += 1
        
        #THESE ARE MIDPOINT VALUES
        plt.plot(self.xi[0], self.yi[0], 'g.', label = 'Midpoint Value')
        plt.plot(self.xi[1], self.yi[1], 'g.')
        plt.plot(self.xi[2], self.yi[2], 'g.')
        plt.plot(self.xi[3], self.yi[3], 'g.')
        plt.plot(self.xi[4], self.yi[4], 'g.')
        plt.plot(self.xi[5], self.yi[5], 'g.')
        
        self.reset()
        
        #Heun Test WITHOUT Iteration
        self.HeunTest(self.ODEfunc,0,5,np.array([3.,0.]),1)
        
        #THESE ARE HEUN VALUES
        plt.plot(self.xi[0], self.yi[0], 'm.', label = 'Heun Value')
        plt.plot(self.xi[1], self.yi[1], 'm.')
        plt.plot(self.xi[2], self.yi[2], 'm.')
        plt.plot(self.xi[3], self.yi[3], 'm.')
        plt.plot(self.xi[4], self.yi[4], 'm.')
        plt.plot(self.xi[5], self.yi[5], 'm.')
        
        #Plotted all datas
        plt.legend()
        plt.grid(True)
        
    #Euler Method Function, only contains mathematical formulas in it.
    def euler_method(self):
        
        self.xi.append(self.xi[self.i] + self.h)
        self.dyi = self.yi[self.i] - self.xi[self.i]**3
        self.calculated = self.yi[self.i] + self.dyi * self.h 
        self.yi.append(self.calculated)
    
    #Reset function
    def reset(self):
        self.i = 0
        self.yi = [3]
        self.h = 1
        self.xi = [0]
        
    #Midpoint method, only contains mathematical formulas again
    def midpoint_method(self):
        
        self.xi.append(self.xi[self.i] + self.h)
        self.k1 = self.yi[self.i] - self.xi[self.i]**3
        self.k2 = self.yi[self.i] + self.k1 * self.h / 2 - (self.xi[self.i] + self.h/2)**3         
        self.calculated = self.yi[self.i] + self.k2 * self.h
        self.yi.append(self.calculated)

    #Defining my diff. func here     
    def ODEfunc(self, t,u):
        y,z = u
        return np.array([ z, -t**3 + y ])


    #Finding k1 and k2 for all steps
    def HeunStep(self, f,t,u,h):
        k1 = h*f(t, u)
        k2 = h*f(t+h, u+k1)
        return u+0.5*(k1+k2)

    #Calculating
    def HeunTest(self, f,a,b,x0,h):
        t = a
        x = x0.copy()
        while t < b+0.5*h:
            self.xi.append(t)
            self.yi.append(x[1])
            x = self.HeunStep(f,t,x,h)
            t=t+h
 
#Calling the object       
if  __name__ == "__main__":
    DiffEquationMethods()
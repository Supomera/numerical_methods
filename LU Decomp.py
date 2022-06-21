#LU Decomposition @Author: Omer Bera Dinc


import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

#Here, I'm defining A matrix of Ax=b equation
A = scipy.array([ [-3.93274430508221, -1.48669698277848, 3.66431315646603, 2.84553384142327, -3.19509001154013],
                  [-0.608588336307769, -1.27637563031236, -1.06595110856869, 3.01866982799001, -4.69929790541700], 
                  [0.573880095544165, -3.97764538038131, -0.461150088411044, -0.365810452987199, -3.70221508869656], 
                  [3.55583682509651, 1.57593190601165, -3.18246240947877, 3.52422629064397, -1.84393903667514],
                  [4.11929354923008, -2.81190141444541,	-4.32561470789425, 1.25647993564420, 2.31534578056076]])

# This is a function to find P, L and U matrices of A; defined them.
P, L, U = scipy.linalg.lu(A)

#I defined b matrix of Ax = b equation.
b = [2.72980317541286, -3.51431234446944, 2.95799583470678, -3.34654722352052, 2.17102915689721]
#To write more clean code, I defined i; I guess this is more understandable while lookin' to understand.
i = len(A)
a1 = (b[i-5])
a2 = (b[i-4] - L[i-4][i-5]*a1)
a3 = (b[i-3] - L[i-3][i-5]*a1 - L[i-3][i-4]*a2)
a4 = (b[i-2] - L[i-2][i-5]*a1 - L[i-2][i-4]*a2 - L[i-2][i-3]*a3)
a5 = (b[i-1] - L[i-1][i-5]*a1 - L[i-1][i-4]*a2 - L[i-1][i-3]*a3 - L[i-1][i-2]*a4)

# While doing LU decomp, we are doing something like LUa=b and first representing Ua as x; after that
# Finding elements of x vector with respect to L and b matrix ABOVE 
# After that, with using the data we found above, we are doing slightly same thing to U matrix and finding solution vector.
c = [a1, a2, a3, a4, a5]
print ("A:")
pprint.pprint(A)

#print ("P:")
#pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)


x5 = c[i-1] / U[i-1][i-1] 
x4 = (c[i-2] - U[i-2][i-1]*x5) / U[i-2][i-2]
x3 = (c[i-3] - U[i-3][i-2]*x4 - U[i-3][i-1]*x5 ) / U[i-3][i-3]
x2 = (c[i-4] - U[i-4][i-3]*x3 - U[i-4][i-2]*x4 - U[i-4][i-1]*x5) / U[i-4][i-4]
x1 = (c[i-5] - U[i-5][i-4]*x2 - U[i-5][i-3]*x3 - U[i-5][i-2]*x4 - U[i-5][i-1]*x5) / U[i-5][i-5]

Solution = [x1, x2, x3, x4, x5]
print("Solution Vector:")
pprint.pprint(Solution)



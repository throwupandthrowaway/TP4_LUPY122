#prog 2
import numpy as np
from scipy.linalg import eigh_tridiagonal
n=100
L=5
dx=L/(n-1)
d=np.zeros(n)
e=np.zeros(n-1)
for i in range(n):
    d[i]=2/(dx**2)

for i in range(n-1):
    e[i]=-1/(dx**2)

w,v=eigh_tridiagonal(d,e)
#prog 4
import numpy as np
from prog2 import v
import matplotlib.pyplot as plt

n=100
L=5
dx=L/(n-1)
x=np.linspace(0,2,100)

def normalize(m,delta_x):
    m/=np.linalg.norm(m,axis=0)
    m/=np.sqrt(delta_x)
    return m

normalize(v,dx)
plt.plot(x,v[0]**2,label=r"$\psi_0$")
plt.plot(x,v[1]**2,label=r"$\psi_1$")
plt.plot(x,v[2]**2,label=r"$\psi_2$")
plt.grid()
plt.legend()
plt.title("3 premiers états propres de la fonction d'onde")
plt.xlabel("p")
plt.ylabel(r"$|\psi_p|^2$")
plt.savefig("Graphe_TP4_Q7_n100_L5.png",bbox_inches="tight")
plt.show()

#prog 2
import numpy as np
from scipy.linalg import eigh_tridiagonal
from prog2 import w
import matplotlib.pyplot as plt
p=np.arange(0,100,1)
L=5
def Etheo(p):
    return (np.pi*(p+1)/L)**2
plt.plot(p,w,label="w")
plt.plot(p,Etheo(p),label=r"$E_p$ théorique")
plt.legend()
plt.grid()
plt.xlabel("p")
plt.ylabel(r"$E_p$")
plt.title("Potentiel en fonction de la position")
plt.savefig("Graphe_TP4_Q6_n100_L5.png",bbox_inches="tight")
plt.show()
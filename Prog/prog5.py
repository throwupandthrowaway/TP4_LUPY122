#prog 5
import numpy as np
from prog2 import v
from prog4 import normalize
import matplotlib.pyplot as plt

n=100
L=5
dx=L/(n-1)
x=np.linspace(0,2,100)

def psi_p_theo(p,x):
    return np.sqrt(2/L)*np.sin(((p+1)*np.pi*(x+L/2))/L)


normalize(v,dx)
plt.plot(x,v[0]**2,label="Expérimental")
plt.plot(x,psi_p_theo(1,x)**2,label="Théorique")
plt.grid()
plt.legend()
plt.title("Premier état propre de la fonction d'onde:"
          +"\n"+"Expérimental vs théorique")
plt.xlabel("x")
plt.ylabel(r"$|\psi_p|^2$")
plt.savefig("Graphe_TP4_Q8_n100_L5.png",bbox_inches="tight")
plt.show()


x=np.linspace(0,0.1,100)
plt.plot(x,v[54]**2,label="Expérimental")
plt.plot(x,psi_p_theo(55,x)**2,label="Théorique")
plt.grid()
plt.legend()
plt.title("55e état propre de la fonction d'onde:"
          +"\n"+"Expérimental vs théorique")
plt.xlabel("x")
plt.ylabel(r"$|\psi_p|^2$")
plt.savefig("Graphe_TP4_Q8_n100_L5_2.png",bbox_inches="tight")
plt.show()

#prog 1
import numpy as np
import matplotlib.pyplot as plt

L=5
n=100
a=1
r1=2
r4=-r1
r2=0.5
r3=-r2
dx=L/(n-1)
hbar=6.62607015e-34/(2*np.pi)
m=hbar**2/2
omega=np.sqrt(1/m)

def potentiel_puits_harmonique(x):
    return (m*omega**2*x**2)/2
def potentiel_puits_double(x):
    return a*(x-r1)*(x-r2)*(x-r3)*(x-r4)

j=np.arange(0,n,1)
x=np.empty(len(j))
for i in j:
    x[i]=-L/2+i*dx

V1=np.zeros(len(x))
V2=potentiel_puits_harmonique(x)
V3=potentiel_puits_double(x)

plt.plot(x,V1,label="Puits carré infini")
plt.plot(x,V2,label="Potentiel harmonique")
plt.plot(x,V3,label="Puits double")
plt.xlabel("x")
plt.ylabel(r"$V(x)$")
plt.title("Potentiel en fonction de la position")
plt.legend()
plt.grid()
plt.savefig("Graphe_TP4_Q2.png",bbox_inches="tight")
plt.show()
